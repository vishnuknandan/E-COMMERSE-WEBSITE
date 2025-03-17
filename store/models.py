from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    description=models.TextField(max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to='images',null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to='images', null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)  # Ensure it cannot be None
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    description = models.TextField(max_length=300, null=False)

    def __str__(self):
        return self.name

    
class cart(models.Model):
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)   
    qty= models.IntegerField(null=False,default=1)
    date=models.DateTimeField(auto_now_add=True)

class Order(models.Model):  # Capitalized the model class name
    orderitem = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    order_sts = models.CharField(max_length=10, default='pending')
    address = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
 
