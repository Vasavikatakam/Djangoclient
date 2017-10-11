# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.from __future__ import unicode_literals
# Create your models here
class households(models.Model):
	id1=models.IntegerField()
	house_id=models.IntegerField()
	Name=models.CharField(max_length=40)
	lat=models.FloatField()
	lon=models.FloatField()
	#yearly_income=models.FloatField()
	#Area=models.FloatField()
	#isfarm=models.BooleanField()
	
