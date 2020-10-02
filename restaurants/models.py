from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    opening_time = models.DateTimeField(blank=True, null=True)
    closing_time = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.name
