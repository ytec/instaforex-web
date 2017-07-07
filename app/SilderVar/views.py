from django.shortcuts import render

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import SilderVarPhotos

class SilderVarViws(CMSPluginBase):
    model = SilderVarPhotos
    name = _("Silder Var Photos")
    render_template = "SilderVar/SilderVar.html"
    cache = False

    def render(self, context, instance, placeholder):

        Photos = SilderVarPhotos.objects.all()
        c = context
        Photo = []
        Photo_url = []
        for i in Photos:
            Photo_url = i.FilePhoto.url
            Photo.append(url)
            print(Photo_url)
        c["Photos"] = Photo
        c["instance"] = instance

        return c

plugin_pool.register_plugin(SilderVarViws)
