from django.db import models

# Create your models here.


class UserDataModel(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} created on {self.date_created} and modified on {self.date_modified}"
