from django.db import models

class Docroot(models.Model):
    user = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    def __unicode__(self):
        return (user, path)
