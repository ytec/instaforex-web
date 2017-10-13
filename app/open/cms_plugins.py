from django.shortcuts import render

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
        
        if FormName == "Real":
            Dicc_name = { 'name' : FormName, }
        elif FormName == "Demo":
            Dicc_name = { 'name' : FormName }
        elif FormName == "Anonymous":
            Dicc_name = { 'name' : FormName }
        else :
            Dicc_name = { 'name' : "Demo" }

        context['open'] = Dicc_name
        print(context['open'])
        return context
plugin_pool.register_plugin(Open)
