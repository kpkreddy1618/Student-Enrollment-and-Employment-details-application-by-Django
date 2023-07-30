from django import forms

class StudForm(forms.Form):
    s_name=forms.CharField(label='Enter the Student Name:',max_length=30)
    s_class=forms.CharField(label='Enter the Student Class:',max_length=30)
    s_address=forms.CharField(label='Enter the Student Address:',max_length=30)
    s_school=forms.CharField(label='Enter the Student School:',max_length=30)
    s_email=forms.EmailField(label='Enter the Student Email:',max_length=30)
class SrchForm(forms.Form):
    s_name=forms.CharField(label='Enter the Student name:',max_length=30)

    