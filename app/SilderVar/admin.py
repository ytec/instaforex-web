from django.contrib import admin
from .models import  SilderVarsPages , SilderVarPhotos
# Register your models here.
class SilderVarAdmin(admin.ModelAdmin):
    list_display = ('Silder Var Photos')


admin.site.register(SilderVarsPages)
admin.site.register(SilderVarPhotos)
