from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
import secrets
# Create your models here.
User    = settings.AUTH_USER_MODEL
Nuser = settings.AUTH_USER_MODEL

class StudentContact(models.Model):
    contact       = PhoneNumberField(blank=False,region="FR",)
    user          = models.ForeignKey(User , default=1 , null=True, on_delete=models.SET_NULL)
    firstname = models.CharField(max_length=40,blank=False,null=False,default="ben")
    lastname = models.CharField(max_length=40,blank=False,null=False,default="bennn")
    contact       = PhoneNumberField(blank=False)


class CompoundV(models.Model):
    borrowRate = models.CharField(max_length=200)
    cash  = models.CharField(max_length=200)
    collateralFactor  = models.CharField(max_length=200)
    exchangeRate  = models.CharField(max_length=200)
    interestRateModelAddress  = models.CharField(max_length=200)
    name  = models.CharField(max_length=200)
    reserves  = models.CharField(max_length=200)
    supplyRate  = models.CharField(max_length=200)
    symbol  = models.CharField(max_length=200)
    ids  = models.CharField(max_length=200,default=2)
    totalBorrows  = models.CharField(max_length=200)
    totalSupply  = models.CharField(max_length=200)
    underlyingAddress  = models.CharField(max_length=200)
    underlyingName  = models.CharField(max_length=200)
    underlyingPrice  = models.CharField(max_length=200)
    underlyingSymbol  = models.CharField(max_length=200)
    reserveFactor  = models.CharField(max_length=200)
    underlyingPriceUSD  = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-dateCreated",)
    def __str__(self) -> str:
        return f"Payment: {str(self.name)}"