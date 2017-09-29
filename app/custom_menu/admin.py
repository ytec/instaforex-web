from django.contrib import admin

from .models import banner, Category, Menu, Pages, page_menu, Sub_Pages_menu

admin.site.register(Category)
admin.site.register(banner)
admin.site.register(Pages)
admin.site.register(page_menu)
admin.site.register(Sub_Pages_menu)
