from django.shortcuts import render
from django.http import request
from suds.client import Client



def openaccountReal(data):
    client = Client('http://client-api.instaforex.com/soapservices/OpenAccount.svc?wsdl')

    openaccountreal = client.factory.create('RealAccount')

    openaccountreal.AccountType['value'] = data.AccountType #-
    #  (AccountType){
    #     value = None
    #     Standard = "Standard"
    #     Eurica = "Eurica"
    #     StandardEUR = "StandardEUR"
    #     StandardRUR = "StandardRUR"
    #     EuricaEUR = "EuricaEUR"
    #     EuricaRUR = "EuricaRUR"
    #  }
    openaccountreal.Address = data.Direcc #-
    openaccountreal.City = data.City #-
    openaccountreal.Country = data.Country #-
    openaccountreal.Domain = None #-
    openaccountreal.Email = data.Email #-
    openaccountreal.IsForMassMarketing = None
    openaccountreal.Leverage = data.Leverage
    openaccountreal.Name = data.Name #-
    openaccountreal.NotificationLanguage['value'] = data.NotificationLanguage #-
    # (Language){
    #  En = "En"
    #  Ru = "Ru"
    # }
    openaccountreal.Phone = data.Phone #-
    openaccountreal.SendEducationalLetter = None
    openaccountreal.State = data.State #-
    openaccountreal.ZipCode = data.ZipCode #-
    openaccountreal.AffiliateCode = data.AffiliateCode #-
    openaccountreal.Currency['value'] = data.Currency
    #   (AccountCurrency){
    #     value = None
    #     USD = "USD"
    #     EUR = "EUR"
    #     RUR = "RUR"
    #     USC = "USC"
    #     EUC = "EUC"
    # }
    openaccountreal.DateOfBirth = data.DateOfBirth
    openaccountreal.IsDesktop = None
    openaccountreal.MobilePhoneOs = None
    openaccountreal.Os = None
    openaccountreal.Resolution = None
    openaccountreal.SwapFree = None
    openaccountreal.TraderType['value'] = None
    #    (TraderType){
    #      value = None
    #      None = "None"
    #      Classic = "Classic"
    #      Binary = "Binary"
    #      Сlassic_and_Binary = "Сlassic_and_Binary"
    #    }

    result = client.service.OpenRealAccount(openaccount)

    pass

def openaccountDemo(data):
    client = Client('http://client-api.instaforex.com/soapservices/OpenAccount.svc?wsdl')

    openaccountdemo = client.factory.create('DemoAccount')

    openaccountdemo.AccountType['value'] = None
    #  (AccountType){
    #     value = None
    #     Standard = "Standard"
    #     Eurica = "Eurica"
    #     StandardEUR = "StandardEUR"
    #     StandardRUR = "StandardRUR"
    #     EuricaEUR = "EuricaEUR"
    #     EuricaRUR = "EuricaRUR"
    #  }
    openaccountdemo.Address = None
    openaccountdemo.City = None
    openaccountdemo.Country = None
    openaccountdemo.Domain = None
    openaccountdemo.Email = None
    openaccountdemo.IsForMassMarketing = None
    openaccountdemo.Leverage = None
    openaccountdemo.Name = None
    openaccountdemo.NotificationLanguage['value'] = None
    # (Language){
    #  En = "En"
    #  Ru = "Ru"
    # }
    openaccountdemo.Phone = None
    openaccountdemo.SendEducationalLetter = None
    openaccountdemo.State = None
    openaccountdemo.ZipCode = None
    openaccountdemo.InitialDeposit = None
    openaccountdemo.AffiliateCode = None
    openaccountdemo.Currency['value'] = None
    #   (AccountCurrency){
    #     value = None
    #     USD = "USD"
    #     EUR = "EUR"
    #     RUR = "RUR"
    #     USC = "USC"
    #     EUC = "EUC"
    # }
    openaccountdemo.InvestorPassword = None
    openaccountdemo.NotSendAccountOpenNotify = None
    openaccountdemo.NotificationLang['value'] = "En"
    # (Language){
    #  En = "En"
    #  Ru = "Ru"
    # }

    result = client.service.OpenDemoAccount(openaccountdemo)

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
