from django.db import models

class Bandwidth(models.Model):
    used = models.CharField(max_length=200)
    quota = models.CharField(max_length=200)
    def __unicode__(self):
        return (self.used, self.quota)

class Graph(models.Model):
    hits_json = models.CharField(max_length=200)
    countries_json = models.CharField(max_length=200)
    def __unicode__(self):
        return (self.hits_json,self.countries_json)
