from django.contrib import admin
from .models import OpenAccountReal, OpenAccountDemo, OpenAccountAnonymous

admin.site.register(OpenAccountReal)
admin.site.register(OpenAccountDemo)
admin.site.register(OpenAccountAnonymous)
