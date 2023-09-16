from django import forms
from django.contrib.auth.forms import UserCreationForm , SetPasswordForm
from django.contrib.auth.models import User
from django.forms import ModelForm , TextInput,EmailInput , PasswordInput,NumberInput
from .models import AdminContact
from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.exceptions import ValidationError


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',"placeholder":"name@example.com"}))
    #firstname= forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First Name"}))
    #lastname= forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Last Name"}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    def clean_email(self):
        emails=self.cleaned_data["email"]
        if User.objects.filter(email=emails).exists():
            raise ValidationError("Email Already Exist. Try Again")
        return emails
    def __init__(self,*arg,**kwarg):
        super(RegisterUserForm,self).__init__(*arg,**kwarg)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Enter username'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['placeholder']='name@example.com'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password '
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
        
        for fieldname in ['username']:
            self.fields[fieldname].help_text = ""
        for fieldname in ['password1']:
            self.fields[fieldname].help_text = ""


class PasswordForm(SetPasswordForm):
    class meta:
        model = get_user_model()
        fields = ['password1','password2']
    def __init__(self,*arg,**kwarg):
        super(PasswordForm,self).__init__(*arg,**kwarg)
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['class']='form-control'

class ContactForm(forms.ModelForm):
    class  Meta:
        model = AdminContact
        fields = ("contact","firstname","lastname")
    def __init__(self,*arg,**kwarg):
        super(ContactForm,self).__init__(*arg,**kwarg)
        self.fields['contact'].widget.attrs['class']='form-control' 
        self.fields['firstname'].widget.attrs['class']='form-control' 
        self.fields['lastname'].widget.attrs['class']='form-control'
        self.fields['contact'].widget=PhoneNumberPrefixWidget(
        #attrs={'class':'menu',"placeholder":"Enter Phone Number"},
        country_attrs={'class':'select mb-2'},
        initial="US",
        country_choices=None,
        number_attrs={'class':'menu',"placeholder":"(555) 555-1234"},
        )

class PasswordForm(SetPasswordForm):
    class meta:
        model = get_user_model()
        fields = ['password1','password2']
    def __init__(self,*arg,**kwarg):
        super(PasswordForm,self).__init__(*arg,**kwarg)
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['class']='form-control'
        self.fields['new_password1'].widget.attrs['placeholder']='New Passworld'
        self.fields['new_password2'].widget.attrs['placeholder']='Confirm Password'

#
        