from django.db import models
from cms.models import CMSPlugin

class name(models.Model):
    name = models.CharField(max_length=25,default="Demo")

    def __str__(self):
        return self.name

class OpenAccountReal(models.Model):
    Name = models.CharField(max_length=25,default="Name")
    SurNames = models.CharField(max_length=100,default="SurName")
    Direcc = models.CharField(max_length=100,default="Direcc")
    Direcc2 = models.CharField(max_length=100,default="Direcc2")
    City = models.CharField(max_length=30,default="City")
    ZipCode = models.CharField(max_length=10,default="ZipCode")
    Country = models.CharField(max_length=30,default="Country")
    State = models.CharField(max_length=30,default="State")
    Email = models.EmailField()
    Phone = models.CharField(max_length=15,default="Phone")
    AccountType = models.CharField(max_length=30,default="AccountType")
    Leverage = models.CharField(max_length=30,default="Leverage")
    NotificationLanguage = models.CharField(max_length=30,default="AccountType")
    Currency = models.CharField(max_length=30,default="Currency")
    DateOfBirth = models.DateTimeField()
    AffiliateCode = models.CharField(max_length=10,default="1234")

class OpenAccountDemo(models.Model):
    Name = models.CharField(max_length=25,default="Name")
    SurNames = models.CharField(max_length=100,default="SurName")
    Direcc = models.CharField(max_length=100,default="Direcc")
    Direcc2 = models.CharField(max_length=100,default="Direcc2")
    City = models.CharField(max_length=30,default="City")
    ZipCode = models.CharField(max_length=10,default="ZipCode")
    Country = models.CharField(max_length=30,default="Country")
    State = models.CharField(max_length=30,default="State")
    Email = models.EmailField()
    Phone = models.CharField(max_length=15,default="Phone")
    AccountType = models.CharField(max_length=30,default="AccountType")
    Leverage = models.CharField(max_length=30,default="Leverage")
    NotificationLanguage = models.CharField(max_length=30,default="AccountType")
    Currency = models.CharField(max_length=30,default="Currency")
    DateOfBirth = models.DateTimeField()
    AffiliateCode = models.CharField(max_length=10,default="1234")
    InitialDeposit = models.CharField(max_length=20,default="1000" )
    InvestorPassword = models.CharField(max_length=30,default="password")

class OpenAccountAnonymous(models.Model):
    Name = models.CharField(max_length=25,default="Name")
    SurNames = models.CharField(max_length=100,default="SurName")
    Direcc = models.CharField(max_length=100,default="Direcc")
    Direcc2 = models.CharField(max_length=100,default="Direcc2")
    City = models.CharField(max_length=30,default="City")
    ZipCode = models.CharField(max_length=10,default="ZipCode")
    Email = models.EmailField()
    Phone = models.CharField(max_length=15,default="Phone")

class form(CMSPlugin):
    Form = models.ForeignKey(name, default=2)
