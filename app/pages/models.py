from django.db import models
from cms.models import Page

class Sub_Pages(models.Model):
    name = models.CharField(max_length=50, default="Pagina")
    description = models.TextField(blank=True)
    titel = models.CharField(max_length=100,
                             default='Titulo pagina ')
    url = models.URLField(max_length=100, blank=True)

    page_external = models.ForeignKey(Page)
    Level = models.CharField(max_length=3, default='1', blank=True)

    def __str__(self):
        return self.name


class page(models.Model):
    name = models.CharField(max_length=50, default="Pagina")
    description = models.TextField(blank=True)
    titel = models.CharField(max_length=100,
                             default='Titulo pagina ')
    url = models.URLField(max_length=100, blank=True)

    page_external = models.ForeignKey(Page)
    Level = models.CharField(max_length=3, default='1', blank=True)

    def __str__(self):
        return self.name
