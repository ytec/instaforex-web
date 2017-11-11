from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import OpenAccountReal, OpenAccountDemo, OpenAccountAnonymous
from .form import FormModelAnonymus, FormModelDemo, FormModelReal
from .soapform import openaccountReal, openaccountDemo, openaccountAnonymous
from .passworsrandom import id_generator


def openAccountReal(request):
    if request.method == "POST":
        print('post')
        form = FormModelReal(request.POST)
        print(form.errors)
        if form.is_valid():
            print('isvalit')
            AccountType = request.POST.get('AccountType')
            #Tienen de estar unidos --------->
            Direcc = request.POST.get('Direcc')
            Direcc2 = request.POST.get('Direcc2')
            #<-------------------------------
            City = request.POST.get('City')
            Country = request.POST.get('Country')
            Domain = request.POST.get('Domain')
            Email = request.POST.get('Email')
            #Nivel de apalancamiento ----->
            Leverage = request.POST.get('Leverage')
            #<-----------------------------
            #Tienen de estar unidos --------->
            Name = request.POST.get('Name')
            SurNames = request.POST.get('SurNames')
            #<-------------------------------
            NotificationLanguage = request.POST.get('NotificationLanguage')
            Phone = request.POST.get('Phone')

            State = request.POST.get('State')
            ZipCode = request.POST.get('ZipCode')
            AffiliateCode = affiliatecCode
            Currency = request.POST.get('Currency')
            DateOfBirth = request.POST.get('DateOfBirth')

            #Datos de los dispositivos ----->

            #<-------------------------------

            language = request.POST.get('language')



            return HttpResponseRedirect('/es/')
        else:
            print('ssnot')
            template = loader.get_template('open/form_direcc.html')
            return HttpResponse(template.render(request))
def openAccountDemo():
    if request.method == "POST":
        form = FormModelDemo(request.POST)
        if FormModel.is_valid():
            AccountType = request.POST.get('AccountType')
            #Tienen de estar unidos --------->
            Direcc = request.POST.get('Direcc')
            Direcc2 = request.POST.get('Direcc2')
            #<-------------------------------
            City = request.POST.get('City')
            Country = request.POST.get('Country')
            Domain = request.POST.get('Domain')
            Email = request.POST.get('Email')

            #Nivel de apalancamiento ----->
            Leverage = request.POST.get('Leverage')
            #<-----------------------------
            #Tienen de estar unidos --------->
            Name = request.POST.get('Name')
            SurNames = request.POST.get('SurNames')
            #<-------------------------------
            NotificationLanguage = request.POST.get('NotificationLanguage')
            Phone = request.POST.get('Phone')

            State = request.POST.get('State')
            ZipCode = request.POST.get('ZipCode')
            InitialDeposit = request.POST.get('InitialDeposit')
            AffiliateCode = affiliatecCode
            Currency = request.POST.get('Currency')

            InvestorPassword = request.POST.get('InvestorPassword')

            DateOfBirth = request.POST.get('DateOfBirth')

            #Datos de los dispositivos ----->

            #<-------------------------------

            language = request.POST.get('language')
            if InvestorPassword == "":
                InvestorPassword = id_generator()
            else:
                pass
            pass

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
