from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name  = models.CharField(max_length=255, blank=True , null=True)
    email      = models.EmailField(max_length=64, blank=True, null=True, default=False)



    def __str__(self):
        return self.username
    

class Investor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investor')
    budget = models.IntegerField()
    project_deadline = models.DateField()

    def __str__(self):
        return self.user.username
    

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')
    name = models.CharField(max_length=255)
    min_investment_amount = models.IntegerField()
    deadline = models.DateField()
    invested = models.BooleanField(default=False)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name