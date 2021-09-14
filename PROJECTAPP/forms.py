from django import forms

class CodeForm(forms.Form):
    text = forms.CharField(label='Your name', max_length=140 )



