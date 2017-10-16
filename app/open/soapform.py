from django.shortcuts import render
from django.http import request
from suds.client import Client

# Create your views here.

def openaccountReal():
    pass

def openaccountDemo():
    pass

def openaccountAnonymous(data):
    client = Client('http://client-api.instaforex.com/soapservices/OpenAccount.svc?wsdl')

    openaccount = client.factory.create('AnonymousAccount')

    openaccount.AffiliateCode = ""
    openaccount.Country = ""
    openaccount.Domain = ""
    openaccount.Email = ""
    openaccount.Name = ""
    openaccount.NotificationLanguage['value'] = "En"
    # (Language){
    #  En = "En"
    #  Ru = "Ru"
    # }
    openaccount.Phone = ""

    result = client.service.OpenAnonymousAccount(openaccount)

    print(result)
