from django.shortcuts import render

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

class Socketio(CMSPluginBase):
    name = _("socket.io")
    render_template = "box.html"
    cache = False

    def render(self, context, instance, placeholder):
        c = context
        if instance:
            pass
        return c
plugin_pool.register_plugin(Socketio)
