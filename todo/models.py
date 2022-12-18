import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
STATE_CHOICES = (
    ('pending','PENDIENTE'),
    ('in progress', 'EN PROCESO'),
    ('finished','FINALIZADO'),
)


class Note(models.Model):
    state = models.CharField(max_length=15, choices=STATE_CHOICES, default='pending')
    description = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCompleted = models.DateTimeField()
    finalDate = models.DateTimeField()

    def __str__(self):
        return self.description + ' - by - ' + self.user.username

    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Note, self).save(*args, **kwargs)

# https://youtu.be/e6PkGDH4wWA?t=4755

# http://localhost:8000/admin/todo/note/add/