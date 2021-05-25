from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Mobile number must be entered in the format: '+9999999999'. Upto 15 digits allowed.")

# Create your models here.
class MobileNumber(models.Model):
    mobile_number = models.CharField(max_length=17, unique=True, validators=[mobile_regex])
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mobile_number}-{self.user.username}"
