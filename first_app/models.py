from django.db import models

# Create your models here.
class StudentForm(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField()
    phone=models.IntegerField()

    def __str__(self):
        return str(self.pk)+" "+ self.first_name
    