from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    cost = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Order(models.Model):
    payment_type = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=True, default=1)
    address = models.CharField(max_length=250, null=False, blank=False)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



class OrderProduct(models.Model):
    count = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)



