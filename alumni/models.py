from django.db import models


class Name(models.Model):
    name_text = models.CharField(max_length=200)
    address_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name_text

    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

