from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image=models.ImageField(upload_to='cars/uploads/',blank=True,null=True)

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE,related_name="comments")
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True) #jokhn ay post er object toirei hobe tokhn sei time ta rekhe dibe
    
    def __str__(self):
        return f"Comment by {self.name}"