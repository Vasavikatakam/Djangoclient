# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from models import households
from django.http import HttpResponse
from django.template import loader
import urllib
import simplejson
import os
from . forms import NameForm

# Create your views here.

"""def insert(request):
	households.objects.all().delete()
		
	link="http://10.0.3.23:8765/House/?format=json"             
	# loading json data coming from the server
	f = urllib.urlopen(link)                               
	myfile = simplejson.load(f)
	listi=[]
	count=0
	# converting it into required form putting data in list in lists 
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['id'])
		listi[count+1].append(myfile[i]['house_id'])
		listi[count+2].append(myfile[i]['Name'])
		listi[count+3].append(myfile[i]['lat'])
		listi[count+4].append(myfile[i]['lon'])
	

	for i in range(0,len(listi[0])):
		r=[]
		for k in listi:
			r.append(k[i])
		households.objects.create(id1=r[0],house_id=r[1],Name=r[2],lat=r[3],lon=r[4])
	l=households.objects.all()
	template=loader.get_template('farmers/polygon.html')
	k=[[1,2,3],[3,4,5],[7,8,9]]
	context={"list1":l}
	return HttpResponse(template.render(context,request))"""

"""def farm(request):
	template=loader.get_template('farmers/polygon.html')
	
	l=[18.383288,  77.868335,
    18.382773, 77.868404,
    
    18.381979, 77.868311,
    
    18.382384,77.867581,
    18.382829,  77.867911,
18.383288,  77.868335]
	k=18.383288
	context={"list":l}
	return HttpResponse(template.render(context,request))"""
"""def house(request):
	template=loader.get_template('farmers/house_point.html')
	l=[18.381877,77.876175]
	k=[[1,2,3],[3,4,5],[7,8,9]]
	context={"lst":	k}
	return HttpResponse(template.render(context,request))"""
def formf(request):
    form = NameForm()
    return render(request, 'farmers/form1.html', {'form': form})

def thanking(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            k=request.POST.get('house_id')   #storing house_id in session variable
            k=int(k)
            request.session['hid']=k

	link="http://10.0.3.23:8765/House/?format=json"
	fpoints_link="http://10.0.3.23:8765/farmpoints/?format=json"
	farm_link="http://10.0.3.23:8765/FarmTable/?format=json"
                                                       #loading json data coming from the web server
	f = urllib.urlopen(link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0                                            # converting it into required form putting data in list in lists 
	
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['house_id'])
		listi[count+1].append(myfile[i]['lat'])
		listi[count+2].append(myfile[i]['lon'])
		listi[count+3].append(myfile[i]['area'])
		listi[count+4].append(myfile[i]['isfarm'])
		listi[count+5].append(myfile[i]['AnnualIncome'])
	l=[]
	for i in range(0,len(listi[0])):                   #extracting house data related to the entered house_id
		if listi[0][i]==k:
			l.append(listi[1][i])
			l.append(listi[2][i])
			l.append(listi[3][i])
			l.append(listi[5][i])
	#images
	image_link="http://10.0.3.23:8765/imagetable/?format=json"

	f = urllib.urlopen(image_link)                      #loading json data coming from the web server
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['house_idi'])              # converting it into required form putting data in list in lists 
	
		listi[count+1].append(myfile[i]['image'])
	imgtable=""
	for i in range(0,len((listi[0]))):
		if listi[0][i]==k:
			imgtable=imgtable+'http://10.0.3.23:8765'+listi[1][i]+','
	#---img close----		
	imgtable=imgtable.rstrip(',')
	str_imgt=imgtable.split(',')
	#videos
	image_link="http://10.0.3.23:8765/videotable/?format=json"

	f = urllib.urlopen(image_link)                         #loading json data coming from the web server   
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	for i in range(0,len(myfile[0])):                      # converting it into required form putting data in list in lists 
	
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['house_idv'])
		listi[count+1].append(myfile[i]['video'])
	vidtable=""
	for i in range(0,len((listi[0]))):
		if listi[0][i]==k:
			vidtable=vidtable+'http://10.0.3.23:8765'+listi[1][i]+','	
	vidtable=vidtable.rstrip(',')
	#----videotable-------
	#strim=str_imgt[0]
	listi=[]
	f = urllib.urlopen(farm_link)                              #loading json data coming from the web server
	myfile1= simplejson.load(f) 
	farm_list=[]
	for i in range(0,len(myfile1[0])):
		list_temp=[]                                            #processing
		listi.append(list_temp)
	for i in range(0,len(myfile1)):
		listi[count].append(myfile1[i]['farm_id'])
		listi[count+1].append(myfile1[i]['area'])
		listi[count+2].append(myfile1[i]['house_farm'])
	m=[]
	m1=[]

	for i in range(0,len(listi[0])):
		if listi[2][i]==k:
			m.append(listi[0][i])
			m1.append(listi[1][i])	
	
	listi=[]
	f = urllib.urlopen(fpoints_link)                                   #loading json data coming from the web server
	myfile2= simplejson.load(f) 
	farm_list=[]
	for i in range(0,len(myfile2[0])):
		list_temp=[]
		listi.append(list_temp)                                       #processing
	for i in range(0,len(myfile2)):
		listi[count].append(myfile2[i]['lat'])
		listi[count+1].append(myfile2[i]['lon'])
		listi[count+2].append(myfile2[i]['farm_idp'])
	n=[]
	if(len(m)!=0):

		for i in m:
			for j in range(0,len(listi[0])):
				if listi[2][j]==i:
					n.append(listi[0][j])
					n.append(listi[1][j])
	mem_link="http://10.0.3.23:8765/mem_details/?format=json"                #loading json data coming from the web server
	f = urllib.urlopen(mem_link)
	myfile3 = simplejson.load(f)  
	listi=[]
	for i in range(0,len(myfile3[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile3)):
		listi[count].append(myfile3[i]['house_idm'])
		listi[count+1].append(myfile3[i]['Name'])

	str1=""
	#str2="vas"
	o=[]
	for i in range(0,len(listi[0])):
		if listi[0][i]==k:
			str1=str1+listi[1][i]+", "
			#o.append(listi[1][i])
	#str1='\n'.join(o)
	str2=str1.rstrip()
	str2=str2.rstrip(',')

	farm_link="http://10.0.3.23:8765/farmcroptable/?format=json"                        #loading json data coming from the web server

	f = urllib.urlopen(farm_link)
	myfile = simplejson.load(f)  
	listi=[]
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['season_id'])
		listi[count+1].append(myfile[i]['crop'])
		listi[count+2].append(myfile[i]['farm_idc'])
	fa=""
	if(len(m)!=0):
		for i in m:
			for j in range(0,len(listi[0])):
				if(listi[2][j]==i):
					fa=fa+listi[1][j]+",";


	fa.rstrip(',')	
		
	well_link="http://10.0.3.23:8765/welltable/?format=json"                          #loading json data coming from the web server

	f = urllib.urlopen(well_link)
	myfile = simplejson.load(f)  
	listi=[]
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['lat'])
		listi[count+1].append(myfile[i]['lon'])
		listi[count+2].append(myfile[i]['depth'])
		listi[count+3].append(myfile[i]['farm_idw'])
	wc=[]
	
	if(len(m)!=0):
		for i in m:	
			for j in range(0,len(listi[0])):
				if listi[3][j]==i:
					wc.append(listi[0][j])
					wc.append(listi[1][j])
					wc.append(listi[2][j])
	


	context={'lst':l,'lst1':n,'lst2':str2,'farea':m1,'crop':fa,'wl':wc,'house_img':imgtable,'house_vid':vidtable}			
	#return HttpResponse(m1)
	return render(request, 'farmers/polygon1.html',context)
	
		






"""def imagere(request):
	image_link="http://10.0.3.23:8765/imagetable/?format=json"

	f = urllib.urlopen(image_link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['image'])
	k2=listi[0][0]
	img1="http://10.0.3.23:8765"+k2
	template=loader.get_template('farmers/thanks.html')
	context={'img':img1}
	return HttpResponse(template.render(context,request))"""
#This is for differentiating family sizes
def housegrp(request):
	link="http://10.0.3.23:8765/House/?format=json"
	#loading json data
	f = urllib.urlopen(link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	#processing
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['house_id'])
		listi[count+1].append(myfile[i]['lat'])
		listi[count+2].append(myfile[i]['lon'])

	
	link="http://10.0.3.23:8765/mem_details/?format=json"

	f = urllib.urlopen(link)
	myfile = simplejson.load(f)  
	listi2=[]
	
	
	#retrieving family size using mem_details table
	for i in range(0,len(myfile)):
		listi2.append(myfile[i]['house_idm'])
	count1=[]
	for i in range(0,len(listi[0])+1):
		count1.append(0)	
	for i in range(0,len(listi2)):
		count1[listi2[i]]=count1[listi2[i]]+1	
	for i in range(0,len(listi[0])):
		listi[count+3].append(count1[i+1])
	context={'totlst':listi}
    #template=loader.get_template('farmers/house_point.html')
  	return render(request,'farmers/familysize.html',context)
def piechart(request):
	farm_link="http://10.0.3.23:8765/farmcroptable/?format=json"

	f = urllib.urlopen(farm_link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	
	for i in range(0,len(myfile)):    #retrieving crops and their count          
		
		listi.append(myfile[i]['crop'])
	
	dict1={}                           #storing crop and their count in a dictionary
	for i in listi:
		if i not in dict1.keys():
			dict1[i]=1
		else:
			dict1[i]=dict1[i]+1

	context={'list':dict1}		
	  	
	return render(request,'farmers/piechart.html',context)
def welldepth(request):
	well_link="http://10.0.3.23:8765/welltable/?format=json"

	f = urllib.urlopen(well_link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	for i in range(0,len(myfile[0])):         #processing

		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):

		listi[count].append(myfile[i]['lat'])
		listi[count+1].append(myfile[i]['lon'])
		listi[count+2].append(myfile[i]['depth'])         #storing lat,lon,depth of a well
		listi[count+3].append(myfile[i]['well_id'])
	#---------wellyield------
	well_link="http://10.0.3.23:8765/wellinfo/?format=json"

	f = urllib.urlopen(well_link)
	myfile = simplejson.load(f)  
	listi2=[]
	count=0
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi2.append(list_temp)
	for i in range(0,len(myfile)):
		listi2[count].append(myfile[i]['well_idf'])        #storing yield of a well
		listi2[count+1].append(myfile[i]['yield1'])
		
	context={'list1':listi,'list2':listi2}
	#------------------close---------
	return render(request,'farmers/welldepth.html',context)	



	
def wellyield(request):
	well_link="http://10.0.3.23:8765/wellinfo/?format=json"

	f = urllib.urlopen(well_link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['well_idf'])     #taking well yield 
		listi[count+1].append(myfile[i]['yield1'])
		
	context={'list1':listi}
	return render(request,'farmers/welldepth.html',context)	
	
def first(request):
	listi=[]
	context={'list1':listi}
	return render(request,'farmers/nav.html',context)   #mainpage


def piemap(request):
	k=request.session['hid']
	#context={'list1':listi}
	#return render(request,'farmers/nav.html',context)


	link="http://10.0.3.23:8765/House/?format=json"
	fpoints_link="http://10.0.3.23:8765/farmpoints/?format=json"
	farm_link="http://10.0.3.23:8765/FarmTable/?format=json"

	f = urllib.urlopen(link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['house_id'])
		listi[count+1].append(myfile[i]['lat'])
		listi[count+2].append(myfile[i]['lon'])
		listi[count+3].append(myfile[i]['area'])
		listi[count+4].append(myfile[i]['isfarm'])
		listi[count+5].append(myfile[i]['AnnualIncome'])
	l=[]
	for i in range(0,len(listi[0])):
		if listi[0][i]==k:
			l.append(listi[1][i])
			l.append(listi[2][i])
			l.append(listi[3][i])
			l.append(listi[5][i])
	#images
	image_link="http://10.0.3.23:8765/imagetable/?format=json"

	f = urllib.urlopen(image_link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['house_idi'])
		listi[count+1].append(myfile[i]['image'])
	imgtable=""
	for i in range(0,len((listi[0]))):
		if listi[0][i]==k:
			imgtable=imgtable+'http://10.0.3.23:8765'+listi[1][i]+','
	#---img close----		
	imgtable=imgtable.rstrip(',')
	str_imgt=imgtable.split(',')
	#videos
	image_link="http://10.0.3.23:8765/videotable/?format=json"

	f = urllib.urlopen(image_link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['house_idv'])
		listi[count+1].append(myfile[i]['video'])
	vidtable=""
	for i in range(0,len((listi[0]))):
		if listi[0][i]==k:
			vidtable=vidtable+'http://10.0.3.23:8765'+listi[1][i]+','	
	vidtable=vidtable.rstrip(',')
	#----videotable-------
	#strim=str_imgt[0]
	listi=[]
	f = urllib.urlopen(farm_link)
	myfile1= simplejson.load(f) 
	farm_list=[]
	for i in range(0,len(myfile1[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile1)):
		listi[count].append(myfile1[i]['farm_id'])
		listi[count+1].append(myfile1[i]['area'])
		listi[count+2].append(myfile1[i]['house_farm'])
	m=[]
	m1=[]

	for i in range(0,len(listi[0])):
		if listi[2][i]==k:
			m.append(listi[0][i])
			m1.append(listi[1][i])	
	
	listi=[]
	f = urllib.urlopen(fpoints_link)
	myfile2= simplejson.load(f) 
	farm_list=[]
	for i in range(0,len(myfile2[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile2)):
		listi[count].append(myfile2[i]['lat'])
		listi[count+1].append(myfile2[i]['lon'])
		listi[count+2].append(myfile2[i]['farm_idp'])
	n=[]
	if(len(m)!=0):

		for i in m:
			for j in range(0,len(listi[0])):
				if listi[2][j]==i:
					n.append(listi[0][j])
					n.append(listi[1][j])
	mem_link="http://10.0.3.23:8765/mem_details/?format=json"
	f = urllib.urlopen(mem_link)
	myfile3 = simplejson.load(f)  
	listi=[]
	for i in range(0,len(myfile3[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile3)):
		listi[count].append(myfile3[i]['house_idm'])
		listi[count+1].append(myfile3[i]['Name'])

	str1=""
	#str2="vas"
	o=[]
	for i in range(0,len(listi[0])):
		if listi[0][i]==k:
			str1=str1+listi[1][i]+", "
			#o.append(listi[1][i])
	#str1='\n'.join(o)
	str2=str1.rstrip()
	str2=str2.rstrip(',')

	farm_link="http://10.0.3.23:8765/farmcroptable/?format=json"

	f = urllib.urlopen(farm_link)
	myfile = simplejson.load(f)  
	listi=[]
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['season_id'])
		listi[count+1].append(myfile[i]['crop'])
		listi[count+2].append(myfile[i]['farm_idc'])
		#listi[count+3].append(myfile[i]['area'])
	fa=""
	if(len(m)!=0):
		for i in m:
			for j in range(0,len(listi[0])):
				if(listi[2][j]==i):
					fa=fa+listi[1][j]+",";


	fa.rstrip(',')	
		
	well_link="http://10.0.3.23:8765/welltable/?format=json"

	f = urllib.urlopen(well_link)
	myfile = simplejson.load(f)  
	listi=[]
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count].append(myfile[i]['lat'])
		listi[count+1].append(myfile[i]['lon'])
		listi[count+2].append(myfile[i]['depth'])
		listi[count+3].append(myfile[i]['farm_idw'])
	wc=[]
	
	if(len(m)!=0):
		for i in m:	
			for j in range(0,len(listi[0])):
				if listi[3][j]==i:
					wc.append(listi[0][j])
					wc.append(listi[1][j])
					wc.append(listi[2][j])
	farm_link="http://10.0.3.23:8765/newfarmcroptable/?format=json"

	f = urllib.urlopen(farm_link)
	myfile = simplejson.load(f)  
	listi=[]
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		
		listi[count].append(myfile[i]['crop'])
		listi[count+1].append(myfile[i]['farm_idnc'])
		listi[count+2].append(myfile[i]['area'])				
	flist=[]
	strc=""
	for i in range(0,len(listi[0])):      #storing farm_id,crop,area in string
		for j in m:
			if(listi[1][i]==j):
				strc=strc+str(j)+','+listi[0][i]+','+str(listi[2][i])+'*'
	strc=strc.strip('*')
				
	


	context={'lst':l,'lst1':n,'lst2':str2,'farea':m1,'crop':fa,'wl':wc,'house_img':imgtable,'house_vid':vidtable,'ncrop':strc,}			
	#return HttpResponse(m1)
	return render(request, 'farmers/piemap1.html',context)

def wateryield(request):
	well_link="http://10.0.3.23:8765/welltable/?format=json"

	f = urllib.urlopen(well_link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):

		listi[count].append(myfile[i]['lat'])
		listi[count+1].append(myfile[i]['lon'])
		listi[count+2].append(myfile[i]['depth'])
		listi[count+3].append(myfile[i]['well_id'])
	#---------wellyield------
	well_link="http://10.0.3.23:8765/wellinfo/?format=json"

	f = urllib.urlopen(well_link)
	myfile = simplejson.load(f)  
	listi2=[]
	count=0
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi2.append(list_temp)
	for i in range(0,len(myfile)):
		listi2[count].append(myfile[i]['well_idf'])
		listi2[count+1].append(myfile[i]['yield1'])
		
	context={'list1':listi,'list2':listi2}
	#------------------close---------
	return render(request,'farmers/wateryield.html',context)	
def annualincome(request):
	link="http://10.0.3.23:8765/House/?format=json"
	
	f = urllib.urlopen(link)
	myfile = simplejson.load(f)  
	listi=[]
	count=0
	
	for i in range(0,len(myfile[0])):
		list_temp=[]
		listi.append(list_temp)
	for i in range(0,len(myfile)):
		listi[count+0].append(myfile[i]['house_id'])         #storing annualincome
		listi[count+1].append(myfile[i]['lat'])
		listi[count+2].append(myfile[i]['lon'])
		listi[count+3].append(myfile[i]['AnnualIncome'])

	context={'list1':listi}
	return render(request,'farmers/annualincome.html',context)

