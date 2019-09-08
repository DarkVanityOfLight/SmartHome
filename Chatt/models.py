from django.db import models

# Create your models here.
class message(models.Model):

    Sender = models.CharField(max_length=20, null=True, blank=True)
    Nachricht = models.TextField()

    def __str__(self):
        return self.Nachricht


class pinned_messages(models.Model):
    pass
    Sender = models.CharField(max_length=20)
    Nachricht = models.TextField()


