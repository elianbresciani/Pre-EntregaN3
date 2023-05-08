from django import forms
 
class PerroForms(forms.Form):
    id=forms.IntegerField()
    nombre = forms.CharField(max_length=30)
    raza = forms.CharField(max_length=30)

class veterinarioForms(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)


class dueñoForms(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
