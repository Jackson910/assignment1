from django.db import models


class Contactus(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.EmailField(max_length=50)
    Message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

