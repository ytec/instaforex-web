from django.contrib import admin

from cms.admin.pageadmin import PageAdmin

from cms.models import Page

from .models import Pages, page, Sub_Pages


admin.site.register(Pages)
admin.site.register(page)
admin.site.register(Sub_Pages)
