from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from suds.client import Client

from .models import OpenAccountReal, OpenAccountDemo, OpenAccountAnonymous
from .form import FormModelAnonymus, FormModelDemo, FormModelReal
from .soapform import openaccountReal, openaccountDemo, openaccountAnonymous
from .passworsrandom import id_generator
from .cms_plugins import Open
from .form_not_if import form_not_if_data


def openAccountReal(request):
    if request.method == "POST":
        form = FormModelReal(request.POST)
        if form.is_valid():

            affiliatecCode = '1234'
            data = []

        #    AccountType = request.POST.get('AccountType'),
            #Tienen de estar unidos --------->
        #    Direcc = request.POST.get('Direcc'),
        #    Direcc2 = request.POST.get('Direcc2'),
            #<-------------------------------
        #    City = request.POST.get('City'),
        #    Country = request.POST.get('Country'),
        #    Domain = request.POST.get('Domain'),
        #    Email = request.POST.get('Email'),
            #Nivel de apalancamiento ----->
        #    Leverage = request.POST.get('Leverage'),
            #<-----------------------------
            #Tienen de estar unidos --------->
        #    Name = request.POST.get('Name'),
        #    SurNames = request.POST.get('SurNames'),
            #<-------------------------------
        #    NotificationLanguage = request.POST.get('NotificationLanguage'),
        #    Phone = request.POST.get('Phone'),

        #    State = request.POST.get('State'),
        #    ZipCode = request.POST.get('ZipCode'),
        #    AffiliateCode = affiliatecCode,
        #    Currency = request.POST.get('AccountCurrency'),
        #    DateOfBirth = request.POST.get('DateOfBirth'),

            #Datos de los dispositivos ----->

            #<-------------------------------

        #    Language = request.POST.get('Language'),

            data.AccountType = request.POST.get('AccountType'),
            data.Direcc = request.POST.get('Direcc'),
            data.Direcc2 = request.POST.get('Direcc2'),
            data.City = request.POST.get('City'),
            data.Country = request.POST.get('Country'),

            data.Email =  request.POST.get('Email'),
            data.Leverage = request.POST.get('Leverage'),
            data.Name = request.POST.get('Name'),
            data.SurNames = request.POST.get('SurNames'),
            data.NotificationLanguage = request.POST.get('Language'),
            data.Phone = request.POST.get('Phone'),
            data.State = request.POST.get('State'),
            data.ZipCode =  request.POST.get('ZipCode'),

            data.Currency =  request.POST.get('AccountCurrency'),
            data.DateOfBirth = request.POST.get('DateOfBirth'),
            data.AffiliateCode = affiliatecCode,
            data.Language = request.POST.get('Language'),

            #  Model Data for form ------>
            openaccountreal = OpenAccountReal(
            AccountType = request.POST.get('AccountType'),
            Direcc = request.POST.get('Direcc'),
            Direcc2 = request.POST.get('Direcc2'),
            City = request.POST.get('City'),
            Country = request.POST.get('Country'),

            Email =  request.POST.get('Email'),
            Leverage = request.POST.get('Leverage'),
            Name = request.POST.get('Name'),
            SurNames = request.POST.get('SurNames'),
            NotificationLanguage = request.POST.get('Language'),
            Phone = request.POST.get('Phone'),
            State = request.POST.get('State'),
            ZipCode =  request.POST.get('ZipCode'),

            Currency =  request.POST.get('AccountCurrency'),
            DateOfBirth = request.POST.get('DateOfBirth'),
            AffiliateCode = affiliatecCode,
            Language = request.POST.get('Language'),
            )

            # fin Model Data for form <----
            openaccountreal.save()
            #openaccountReal(data)

            return HttpResponseRedirect('/es/')
        else:
            Dicc_name_return = form_not_if_data.Real()
            return render(request, 'open/form_direcc.html', {
            'form':form,
            'open':Dicc_name,
            })
            #template = loader.get_template('open/form_direcc.html')
            #return HttpResponse(template.render(request))
            for d in Dicc_name_return.AccountType:
                print(d)
    else:
        Dicc_name_return = form_not_if_data.Real()
        return render(request, 'open/form_direcc.html', {
        'open':Dicc_name_return,
        })
        for d in Dicc_name_return.AccountType:
            print(d)

def openAccountDemo():
    if request.method == "POST":
        form = FormModelDemo(request.POST)
        if FormModel.is_valid():
            affiliatecCode = '1234'
            data = []

        #    AccountType = request.POST.get('AccountType'),
            #Tienen de estar unidos --------->
        #    Direcc = request.POST.get('Direcc'),
        #    Direcc2 = request.POST.get('Direcc2'),
            #<-------------------------------
        #    City = request.POST.get('City'),
        #    Country = request.POST.get('Country'),
        #    Domain = request.POST.get('Domain'),
        #    Email = request.POST.get('Email'),
            #Nivel de apalancamiento ----->
        #    Leverage = request.POST.get('Leverage'),
            #<-----------------------------
            #Tienen de estar unidos --------->
        #    Name = request.POST.get('Name'),
        #    SurNames = request.POST.get('SurNames'),
            #<-------------------------------
        #    NotificationLanguage = request.POST.get('NotificationLanguage'),
        #    Phone = request.POST.get('Phone'),

        #    State = request.POST.get('State'),
        #    ZipCode = request.POST.get('ZipCode'),
        #    AffiliateCode = affiliatecCode,
        #    Currency = request.POST.get('AccountCurrency'),
        #    DateOfBirth = request.POST.get('DateOfBirth'),

            #Datos de los dispositivos ----->

            #<-------------------------------

        #    Language = request.POST.get('Language'),

            data.AccountType = request.POST.get('AccountType'),
            data.Direcc = request.POST.get('Direcc'),
            data.Direcc2 = request.POST.get('Direcc2'),
            data.City = request.POST.get('City'),
            data.Country = request.POST.get('Country'),

            data.Email =  request.POST.get('Email'),
            data.Leverage = request.POST.get('Leverage'),
            data.Name = request.POST.get('Name'),
            data.SurNames = request.POST.get('SurNames'),
            data.NotificationLanguage = request.POST.get('Language'),
            data.Phone = request.POST.get('Phone'),
            data.State = request.POST.get('State'),
            data.ZipCode =  request.POST.get('ZipCode'),

            data.Currency =  request.POST.get('AccountCurrency'),
            data.DateOfBirth = request.POST.get('DateOfBirth'),
            data.AffiliateCode = affiliatecCode,
            data.Language = request.POST.get('Language'),

            #  Model Data for form ------>
            openaccountreal = OpenAccountReal(
            AccountType = request.POST.get('AccountType'),
            Direcc = request.POST.get('Direcc'),
            Direcc2 = request.POST.get('Direcc2'),
            City = request.POST.get('City'),
            Country = request.POST.get('Country'),

            Email =  request.POST.get('Email'),
            Leverage = request.POST.get('Leverage'),
            Name = request.POST.get('Name'),
            SurNames = request.POST.get('SurNames'),
            NotificationLanguage = request.POST.get('Language'),
            Phone = request.POST.get('Phone'),
            State = request.POST.get('State'),
            ZipCode =  request.POST.get('ZipCode'),

            Currency =  request.POST.get('AccountCurrency'),
            DateOfBirth = request.POST.get('DateOfBirth'),
            AffiliateCode = affiliatecCode,
            Language = request.POST.get('Language'),
            )

            # fin Model Data for form <----
            openaccountreal.save()
            #openaccountReal(data)

            return HttpResponseRedirect('/es/')
        else:
            Dicc_name_return = form_not_if.Demo()
            return render(request, 'open/form_direcc.html', {
            'form':form,
            'open':Dicc_name,
            })
            #template = loader.get_template('open/form_direcc.html')
            #return HttpResponse(template.render(request))
    else:
        Dicc_name_return = form_not_if.Demo()
        return render(request, 'open/form_direcc.html', {
        'open':Dicc_name_return,
        })

def openAccountAnonymous():
    if request.method == "POST":
        form = FormModelAnonymus(request.POST)
        if form.is_valid():
            Name = request.POST.get('Name')
            SurNames = request.POST.get('SurNames')
            Direcc = request.POST.get('Direcc')
            Direcc2 = request.POST.get('Direcc2')
            City = request.POST.get('City')
            ZipCode = request.POST.get('ZipCode')
            language = request.POST.get('language')
            email = request.POST.get('Email')
            Phone = request.POST.get('Phone')


            return redirect('post_detail', pk=post.pk)
    else:
        pass
