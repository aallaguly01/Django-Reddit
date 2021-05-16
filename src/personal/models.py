from django.db import models

# Create your models here.

PRIORITY = [
    ("H", "High"),
    ("M", "Medium"),
    ("L", "Low"),
]

class Questions(models.Model):
    title = models.CharField(max_length=60)
    question = models.TextField(max_length=400)
    priority = models.CharField(max_length=1, choices=PRIORITY)

    def __str__(self):
        return self.title

    # Meta class changes table names in admin site
    class Meta:
        verbose_name = "The Questions"
        verbose_name_plural = "People Questions"
