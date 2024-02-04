from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name} - {self.order_date}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


# CRUD functions
def create_client(name, email, phone_number, address):
    client = Client(name=name, email=email, phone_number=phone_number, address=address)
    client.save()
    return client


def read_client(client_id):
    client = Client.objects.get(id=client_id)
    return client


def update_client(client_id, name=None, email=None, phone_number=None, address=None):
    client = Client.objects.get(id=client_id)
    if name:
        client.name = name
    if email:
        client.email = email
    if phone_number:
        client.phone_number = phone_number
    if address:
        client.address = address
    client.save()
    return client


def delete_client(client_id):
    client = Client.objects.get(id=client_id)
    client.delete()


def create_product(name, description, price, quantity):
    product = Product(name=name, description=description, price=price, quantity=quantity)
    product.save()
    return product


def read_product(product_id):
    product = Product.objects.get(id=product_id)
    return product


def update_product(product_id, name=None, description=None, price=None, quantity=None):
    product = Product.objects.get(id=product_id)
    if name:
        product.name = name
    if description:
        product.description = description
    if price:
        product.price = price
    if quantity:
        product.quantity = quantity
    product.save()
    return product


def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()


def create_order(client_id, products, total_amount):
    client = Client.objects.get(id=client_id)
    order = Order(client=client, total_amount=total_amount)
    order.save()
    for product_id, quantity in products.items():
        product = Product.objects.get(id=product_id)
        order_item = OrderItem(order=order, product=product, quantity=quantity)
        order_item.save()
    return order
