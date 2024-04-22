from django.db import models
class data(models.Model):
    title = models.CharField(max_length=300, default='')
    completed = models.BooleanField(default=False)
    task = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.title
# Create your models here.
