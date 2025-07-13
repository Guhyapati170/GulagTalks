from django.db import models

# Create your models here.

class SIGNUP(models.Model):
    Name=models.CharField(max_length=50)
    Phone_number=models.IntegerField()
    Age=models.IntegerField()
    Gender=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Education=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name    


    