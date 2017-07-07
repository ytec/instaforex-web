from django.db import models
from cms.models import CMSPlugin
from cms.models import Page


class BonusHomePost(models.Model):
    ''' SilderVar model. '''
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=100, blank=True)
    titel = models.CharField(max_length=30, default='instaforex')
    text = models.TextField(max_length=100, blank=True)
    link = models.CharField(max_length=100, default='instaforex')
    botton = models.CharField(max_length=25)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class BonusHomePage(CMSPlugin):
    name = models.CharField(max_length=50, default="Home")
    Post = models.ManyToManyField(BonusHomePost)
    page = models.ForeignKey(Page)

    def __str__(self):
        return self.name

    def copy_relations(self, oldinstance):
        self.Post = oldinstance.Post.all()
