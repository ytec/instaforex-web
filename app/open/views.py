from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import OpenAccountReal, OpenAccountDemo, OpenAccountAnonymous
from .form import FormModel
from .soapform import openaccountReal, openaccountDemo, openaccountAnonymous


def openAccountReal(request):
    if request.method == "POST":
        print('post')
        form = FormModel(request.POST)
        print(form.errors)
        if form.is_valid():
            print('isvalit')
            AccountType = request.POST.get('AccountType')
            #Tienen de estar unidos --------->
            direcc = request.POST.get('direcc')
            direcc2 = request.POST.get('direcc2')
            #<-------------------------------
            city = request.POST.get('city')
            Country = request.POST.get('Country')
            Domain = request.POST.get('Domain')
            Email = request.POST.get('Email')
            #Nivel de apalancamiento ----->
            Leverage = request.POST.get('Leverage')
            #<-----------------------------
            #Tienen de estar unidos --------->
            name = request.POST.get('name')
            surnames = request.POST.get('surnames')
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




            #Is For Mass Marketing
            IsForMassMarketing = ''
            OpenAccountReal.name = name
            print(name)
            template = loader.get_template('open/register.html')
            print(form)
            form.clean()
            print(form)
            return HttpResponseRedirect('/es/')
        else:
            print('ssnot')
            template = loader.get_template('open/form_direcc.html')
            return HttpResponse(template.render(request))
def openAccountDemo():
    if request.method == "POST":
        form = FormModel(request.POST)
        if FormModel.is_valid():
            AccountType = request.POST.get('AccountType')
            #Tienen de estar unidos --------->
            direcc = request.POST.get('direcc')
            direcc2 = request.POST.get('direcc2')
            #<-------------------------------
            city = request.POST.get('city')
            Country = request.POST.get('Country')
            Domain = request.POST.get('Domain')
            Email = request.POST.get('Email')

            #Nivel de apalancamiento ----->
            Leverage = request.POST.get('Leverage')
            #<-----------------------------
            #Tienen de estar unidos --------->
            name = request.POST.get('name')
            surnames = request.POST.get('surnames')
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

            pass

def openAccountAnonymous():
    if request.method == "POST":
        form = FormModel(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            surnames = request.POST.get('surnames')
            direcc = request.POST.get('direcc')
            direcc2 = request.POST.get('direcc2')
            city = request.POST.get('city')
            cp = request.POST.get('cp')
            language = request.POST.get('language')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')


            return redirect('post_detail', pk=post.pk)
    else:
        pass
