from django.db import models
from django.contrib.auth.models import User

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    earned_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')

    def __str__(self):
        return f"{self.title} ({self.category})"