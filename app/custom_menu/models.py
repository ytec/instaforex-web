from django.db import models
from cms.models import CMSPlugin
from cms.models import Page

from app.pages.models import page, Sub_Pages

class Sub_Pages_menu(models.Model):
    name = models.CharField(max_length=50, default="Pagina")
    Icon = models.FileField(upload_to='Custom_Menu/img',
                            default='Custom_Menu/img/icon/default.png')
    X = models.CharField(max_length=4, blank=True)
    Y = models.CharField(max_length=4, blank=True)
    page = models.ForeignKey(Sub_Pages, default=1)

    def __str__(self):
        return self.name

class page_menu(models.Model):
    name = models.CharField(max_length=50, default="Pagina")
    Icon = models.FileField(upload_to='Custom_Menu/img',
                            default='Custom_Menu/img/icon/default.png')
    X = models.CharField(max_length=4, blank=True)
    Y = models.CharField(max_length=4, blank=True)
    page = models.ForeignKey(page, default=1)

    def __str__(self):
        return self.name
class Pages(models.Model):
    name = models.CharField(max_length=50, default="Pagina")
    Pages = models.ManyToManyField(page_menu, blank=True)
    Sub_Pages = models.ManyToManyField(Sub_Pages_menu, blank=True)
    def __str__(self):
        return self.name

class banner(models.Model):
    name = models.CharField(max_length=50, default="Pagina")
    description = models.TextField(blank=True)
    Imagen = models.FileField(upload_to='Custom_Menu/img/Banner_img',
                              default='Custom_Menu/img/Banner_img/default.png')
    url = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, default="Category")
    titel = models.CharField(max_length=100,
                             default='Pagina_cms o pagina externa')
    Level = models.CharField(max_length=3, default='0')
    url = models.URLField(max_length=100, blank=True)
    Banner = models.ManyToManyField(banner, blank=True)
    Pages = models.ManyToManyField(Pages, blank=True)

    def __str__(self):
        return self.name

class Menu(CMSPlugin):
    name = models.CharField(max_length=50, default="menu")
    titel = models.CharField(max_length=100,
                             default='Titulo Menu')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def copy_relations(self, oldinstance):
        self.category = oldinstance.category.all()
