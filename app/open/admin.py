from django.contrib import admin
from .models import OpenAccountReal, OpenAccountDemo, OpenAccountAnonymous
from .imports import data_forms


class ImportsoapAdmin(admin.ModelAdmin,):
    change_list_template = "open/admin/inport.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('inport/', self.set_inport),
            ]
        return my_urls + urls

    def set_inport(self, request):
        self.model.objects.all().update(is_immortal=True)
        self.message_user(request, "All heroes are now immortal")
        return HttpResponseRedirect("../")


admin.site.register(OpenAccountReal)
admin.site.register(OpenAccountDemo)
admin.site.register(OpenAccountAnonymous)
