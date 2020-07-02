from django import forms

class SearchDataForm(forms.Form):
    Bank=forms.CharField(max_length=49,required=True)
    City=forms.CharField(max_length=50,required=True)

class SearchIFSCForm(forms.Form):
    IFSCCode=forms.CharField(max_length=11,required=True)

