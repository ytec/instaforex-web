from django.shortcuts import render

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .views import Custom_menu_data

from .models import Category, Menu

class custom_menu(CMSPluginBase):
    model = Menu
    name = _("Custom menu")
    render_template = "menu.html"
    cache = False


    def render(self, context, instance, placeholder,):
        context['Menus'] = Custom_menu_data.get(instance.pk)
        return context
plugin_pool.register_plugin(custom_menu)
