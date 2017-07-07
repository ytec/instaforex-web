from django.shortcuts import render

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import SilderVarsPages, SilderVarPhotos

class SilderVarPlugin(CMSPluginBase):
    model = SilderVarsPages
    name = _("Silder Var")
    render_template = "SilderVar/SilderVar.html"
    cache = False

    def render(self, context, instance, placeholder):
        c = context
        Photos = []
        Photo = []
        for l in SilderVarsPages.objects.all():
            for x in l.Photo.all():
                Photo = x.FilePhoto.url
                Photos.append(Photo)
        c['photos'] = Photos

        return c
plugin_pool.register_plugin(SilderVarPlugin)
