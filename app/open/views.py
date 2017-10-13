from django import forms
from django.http import HttpResponse
from django.template import loader

from .models import OpenAccountReal, OpenAccountDemo, OpenAccountAnonymous
from .form import FormModel

def openAccountReal(request):
    if request.method == "POST":
        if FormModel.is_valid():
            name = request.POST.get('full_name')
            print(name)
            template = loader.get_template('open/register.html')
            return HttpResponse(template.render(request))
    else:
        template = loader.get_template('open/form_direcc.html')
        return HttpResponse(template.render(request))
def openAccountDemo():
    if request.method == "POST":
        if FormModel.is_valid():
            pass

def openAccountAnonymous():
    if request.method == "POST":
        if form.is_valid():
            return redirect('post_detail', pk=post.pk)
    else:
        pass
