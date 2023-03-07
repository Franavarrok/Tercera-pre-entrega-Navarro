from django import forms

class SchoolForm(forms.Form):

    name = forms.CharField()
    address = forms.CharField()
    phone = forms.IntegerField()
    gmail = forms.EmailField()

class ProfessorForm (forms.Form):

    name = forms.CharField()
    occupation = forms.CharField()
    age = forms.IntegerField()
    phone = forms.IntegerField()
    gmail = forms.EmailField()

class StudentForm (forms.Form):

    name = forms.CharField()
    surname = forms.CharField()   
    grade = forms.IntegerField()
    age = forms.IntegerField()
    phone = forms.IntegerField()
    gmail = forms.EmailField()