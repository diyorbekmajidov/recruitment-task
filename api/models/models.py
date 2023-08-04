from django.db import models
from django.contrib.auth. models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    

class Investor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.IntegerField()
    project_deadline = models.DateField()

    def __str__(self):
        return self.user.email
    

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    min_investment_amount = models.IntegerField()
    deadline = models.DateField()
    invested = models.BooleanField(default=False)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name