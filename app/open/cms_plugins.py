from django.shortcuts import render

from suds.client import Client

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import form

class Open(CMSPluginBase):
    model = form
    name = _("Formulario")
    render_template = "open/form.html"
    cache = False

    def render(self, context, instance, placeholder):
        Form = form.objects.get(pk=instance.pk)
        FormName = Form.Form.name
        c = context
        client = Client('http://client-api.instaforex.com/soapservices/OpenAccount.svc?wsdl')

        if FormName == "Real":
            AccountType = client.factory.create('AccountType')
            Dicc_AccountType = []
            for s in AccountType:
                d = {s[0] : s[1]}
                Dicc_AccountType.append(d)

            Language = client.factory.create('Language')
            AccountCurrency = client.factory.create('AccountCurrency')
            TraderType = client.factory.create('TraderType')
            Dicc_name = { 'name' : FormName,
                          'AccountType' : Dicc_AccountType,
                          'Language' : Language,
                          'AccountCurrency' : AccountCurrency,
                          'TraderType' : TraderType,
                        }
            print(Dicc_name)
        elif FormName == "Demo":

            Dicc_name = { 'name' : FormName }

        elif FormName == "Anonymous":
            Dicc_name = { 'name' : FormName }
        else :
            Dicc_name = { 'name' : "Demo" }

        context['open'] = Dicc_name
        return context
plugin_pool.register_plugin(Open)
