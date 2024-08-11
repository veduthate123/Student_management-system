from django.db import models

# Create your models here. tabel database

class Student_information(models.Model):
    student_id = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.CharField(max_length=30)
    Number = models.CharField(max_length=20)
    Date = models.DateField()
    Student_Image = models.ImageField(upload_to="images",max_length=350,default="")
    
    def __str__(self):
        return self.First_name
    
    
class Sign_up(models.Model):
    sign_id = models.AutoField(primary_key=True)
    sign_name = models.CharField(max_length=50)
    sign_email = models.CharField(max_length=30)
    sign_pass = models.CharField(max_length=20)
    
    def __str__(self):
        return self.sign_name
    