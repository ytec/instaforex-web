from django.db import models
from cms.models import CMSPlugin

class name(models.Model):
    name = models.CharField(max_length=25,default="Demo")

    def __str__(self):
        return self.name    

class OpenAccountReal(models.Model):
    Form = models.ForeignKey(name, default=1)

class OpenAccountDemo(models.Model):
    Form = models.ForeignKey(name, default=2)

class OpenAccountAnonymous(models.Model):
    Form = models.ForeignKey(name, default=3)

class form(CMSPlugin):
    Form = models.ForeignKey(name, default=2)
