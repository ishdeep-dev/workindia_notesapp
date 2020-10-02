from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django_cryptography.fields import encrypt


class Note(models.Model):
    note = encrypt(models.TextField(max_length=360))
