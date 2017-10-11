from django import forms

class NameForm(forms.Form):
    house_id= forms.IntegerField(label='House_id')