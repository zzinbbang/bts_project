from django.db import models

# Create your models here.
class Btsuser(models.Model):
    fname = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50,null=True)
    birthday = models.DateField()
    country = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField()
    zip = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=100,null=True)
    anotheraddress= models.CharField(max_length=100,null=True)
    usercode = models.CharField(max_length=6,null=True)
    def __str__(self):
        return self.fname