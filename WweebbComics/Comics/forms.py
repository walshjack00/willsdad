from django import forms

class JobForm(forms.Form):
    your_job = forms.CharField(label='Your Job' , max_length=100)