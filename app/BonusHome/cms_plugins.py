from django.shortcuts import render

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import BonusHomePage, BonusHomePost

class HomeBonus(CMSPluginBase):
    model = BonusHomePage
    name = _("Bonus Home")
    render_template = "boxs.html"
    cache = False

    def render(self, context, instance, placeholder):
        p = BonusHomePage.objects.all()
        c = context
        blocksbonus  = []
        for f in p:
            if f.Post.all():
                for z in f.Post.all():
                    block = {
                            'titel' : z.titel,
                            'text' : z.text,
                            'link' : z.link,
                            'botton' :z.botton,
                            'name' : z.name,
                            }
                    blocksbonus.append(block)
                if block:
                    c['blocksbonus'] = blocksbonus
        return c
plugin_pool.register_plugin(HomeBonus)
