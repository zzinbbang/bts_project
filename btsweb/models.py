from django.db import models

# Create your models here.
class Btsuser(models.Model):
    fname = models.CharField(max_length=50,null=False)
    lname = models.CharField(max_length=50,null=False)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField()
    address = models.CharField(max_length=100,null=False)
    birthday = models.DateField()
    usercode = models.CharField(max_length=6,null=True)
    def __str__(self):
        return self.fname