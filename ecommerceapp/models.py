from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(blank=False, null=False)
    school = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name