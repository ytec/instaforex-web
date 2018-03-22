from django.shortcuts import render

from suds.client import Client

from .form_not_if import form_not_if_data


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

        if FormName == "Real":
            Dicc_name = form_not_if_data.Real()


        elif FormName == "Demo":
            Dicc_name = form_not_if_data.Demo()


        elif FormName == "Anonymous":

            Dicc_name = { 'name' : FormName }

        else :
            Dicc_name = form_not_if_data.Demo()

        context['open'] = Dicc_name
        context['form'] = form

        return context
plugin_pool.register_plugin(Open)
