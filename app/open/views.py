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

            name = request.POST.get('name')
            surnames = request.POST.get('surnames')
            direcc = request.POST.get('direcc')
            direcc2 = request.POST.get('direcc2')
            city = request.POST.get('city')
            cp = request.POST.get('cp')
            language = request.POST.get('language')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')

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
            pass

def openAccountAnonymous():
    if request.method == "POST":
        form = FormModel(request.POST)
        if form.is_valid():
            return redirect('post_detail', pk=post.pk)
    else:
        pass
