from django.db import models
from cms.models import CMSPlugin
from cms.models import Page


class SilderVarPhotos(models.Model):
    ''' SilderVar model. '''
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    FilePhoto = models.FileField(upload_to='SilderVar/img', default='SilderVar/img/default.png')
    url = models.URLField(max_length=100, blank=True)
    titel = models.CharField(max_length=100, default='instaforex')
    text = models.TextField(blank=True)
    link = models.CharField(max_length=100, default='instaforex')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class SilderVarsPages(CMSPlugin):
    name = models.CharField(max_length=50, default="Home")
    Photo = models.ManyToManyField(SilderVarPhotos)
    page = models.ForeignKey(Page)

    def __str__(self):
        return self.name

    def copy_relations(self, oldinstance):
        self.Photo = oldinstance.Photo.all()
