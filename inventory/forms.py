from django import forms
from .models import *

class HSCForm(forms.ModelForm):
    class Meta:
        model = HSC
        fields = ('Record_ID', 'Record_Type', 'Campaign_ID', 'Campaign', 'Budget', 'Portofolio_ID', 'Campaign_Start_Date')


class PPCForm(forms.ModelForm):
    class Meta:
        model = PPC
        fields = ('Record_ID', 'Record_Type', 'Campaign_ID', 'Campaign', 'Budget', 'Portofolio_ID', 'Campaign_Start_Date')
        

class BidoptForm(forms.ModelForm):
    class Meta:
        model = Bidopt
        fields = ('Record_ID', 'Record_Type', 'Campaign_ID', 'Campaign', 'Budget', 'Portofolio_ID', 'Campaign_Start_Date')