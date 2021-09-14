from django.db import models

# Create your models here.
class Code(models.Model):
    text = models.CharField(max_length=200)
    code = models.CharField(max_length=400)


def save(self, *args, **kwargs):
    self.username = self.username.lower()
    return super(User, self).save(*args, **kwargs)