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
            Dicc_AccountType = []
            Dicc_Language = []
            Dicc_AccountCurrency = []
            Dicc_TraderType = []

            AccountType = client.factory.create('AccountType')

            for s in AccountType:
                d = { 'name' : s[0],
                      'value' : s[1]}
                Dicc_AccountType.append(d)

            Language = client.factory.create('Language')

            for a in Language:
                h = {'name' : a[0],
                    'value' : a[1]}
                Dicc_Language.append(h)

            AccountCurrency = client.factory.create('AccountCurrency')

            for q in AccountCurrency:
                f = {'name' : q[0],
                    'value' : q[1]}
                Dicc_AccountCurrency.append(f)

            #TraderType = client.factory.create('TraderType')

            #for z in TraderType:
            #    e = {'name' : z[0],
            #        'value' : z[1]}
            #    Dicc_TraderType.append(e)

            Dicc_name = { 'name' : FormName,
                          'AccountType' : Dicc_AccountType,
                          'Language' : Dicc_Language,
                          'AccountCurrency' : Dicc_AccountCurrency,
            #              'TraderType' : Dicc_TraderType,
                        }

        elif FormName == "Demo":

            Dicc_AccountType = []
            Dicc_Language = []
            Dicc_AccountCurrency = []
            Dicc_TraderType = []

            AccountType = client.factory.create('AccountType')

            for s in AccountType:
                d = {'name' : s[0],
                    'value' : s[1]}
                Dicc_AccountType.append(d)

            Language = client.factory.create('Language')

            for a in Language:
                h = {'name' : a[0],
                    'value' : a[1]}
                Dicc_Language.append(h)

            AccountCurrency = client.factory.create('AccountCurrency')

            for q in AccountCurrency:
                f = {'name' : q[0],
                    'value' : q[1]}
                Dicc_AccountCurrency.append(f)

            TraderType = client.factory.create('TraderType')

            for z in TraderType:
                e = {'name' : z[0],
                    'value' : z[1]}
                Dicc_TraderType.append(e)

            Dicc_name = { 'name' : FormName,
                          'AccountType' : Dicc_AccountType,
                          'Language' : Dicc_Language,
                          'AccountCurrency' : Dicc_AccountCurrency,
                          'TraderType' : Dicc_TraderType,
                        }

        elif FormName == "Anonymous":

            Dicc_name = { 'name' : FormName }

        else :

            Dicc_AccountType = []
            Dicc_Language = []
            Dicc_AccountCurrency = []
            Dicc_TraderType = []

            AccountType = client.factory.create('AccountType')

            for s in AccountType:
                d = {'name' : s[0],
                    'value' : s[1]}
                Dicc_AccountType.append(d)

            Language = client.factory.create('Language')

            for a in Language:
                h = {'name' : a[0],
                    'value' : a[1]}
                Dicc_Language.append(h)

            AccountCurrency = client.factory.create('AccountCurrency')

            for q in AccountCurrency:
                f = {'name' : q[0],
                    'value' : q[1]}
                Dicc_AccountCurrency.append(f)

            TraderType = client.factory.create('TraderType')

            for z in TraderType:
                e = {'name' : z[0],
                    'value' : z[1]}
                Dicc_TraderType.append(e)

            Dicc_name = { 'name' : FormName,
                          'AccountType' : Dicc_AccountType,
                          'Language' : Dicc_Language,
                          'AccountCurrency' : Dicc_AccountCurrency,
                          'TraderType' : Dicc_TraderType,
                        }

        context['open'] = Dicc_name
        context['form'] = form
        print(form)
        return context
plugin_pool.register_plugin(Open)
