from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models .EmailField()
    phone = models.CharField(max_length=20)
    about = models.TextField()
    skills = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    achievements = models.CharField(max_length=255)