from django.db import models
from cms.models import Page

from app.subpages.models import Sub_Pages

class page(models.Model):
    name = models.CharField(max_length=50, default="Pagina")
    description = models.TextField(blank=True)
    titel = models.CharField(max_length=100,
                             default='Titulo pagina ')
    url = models.URLField(max_length=100, blank=True)
    Icon = models.FileField(upload_to='Custom_Menu/img',
                            default='Custom_Menu/img/icon/default.png')
    X = models.CharField(max_length=4, blank=True)
    Y = models.CharField(max_length=4, blank=True)
    page_external = models.ForeignKey(Page)
    subpages = models.ManyToManyField(Sub_Pages, blank=True)
    Level = models.CharField(max_length=3, default='1', blank=True)

    def __str__(self):
        return self.name
