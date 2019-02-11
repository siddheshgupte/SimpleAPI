from django.db import models

# Create your models here.


class UserDataModel(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=True, default=None)
    contact_number = models.TextField(max_length=10, blank=True, default=None)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, default='M')
    birth_date = models.DateField(blank=True, default=None, null=True)
    left_leg_len = models.DecimalField(decimal_places=5, max_digits=5, blank=True, default=False)
    right_leg_len = models.DecimalField(decimal_places=5, max_digits=5, blank=True, default=False)
    weight = models.DecimalField(decimal_places=5, max_digits=5, blank=True, default=False)
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} created on {self.date_created} and modified on {self.date_modified}"
