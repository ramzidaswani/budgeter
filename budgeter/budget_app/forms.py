from django import forms
from budgeter.models import Customer

from django.contrib.auth import get_user_model
User = get_user_model()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserInfo(forms.ModelForm):
    name = forms.CharField()
    bank_name = forms.CharField()

    
class ExpensesForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    amount = forms.IntegerField()
