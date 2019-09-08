from django.db import models

# Create your models here.
class important_thing(models.Model):

    Ersteller = models.CharField(max_length=30)
    Datum = models.DateField(verbose_name="Datum")
    body = models.TextField()

    def __str__(self):
        return self.bodys
