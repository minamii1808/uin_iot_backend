from django.db import models

# Create your models here.
class stats(models.Model):
    temperature = models.fields.FloatField()
    humadity = models.fields.FloatField()

    def _str_(self):
        return f'Temp = {self.temperature} dan Humadity = {self.humadity}'
