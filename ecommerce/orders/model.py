from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
#This code defines a Customer model with two fields:
#name: A character field to store the customer's name.
#email: An email field that must be unique for each customer.
#__str__() method is used to define how a Customer object is represented as a string.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} for {self.customer.name} - {self.total_amount}"
#This code defines an Order model with three fields:
#customer: A foreign key relationship with the Customer model. This indicates that an order belongs to one customer.
#order_date: A date field that is automatically set to the current date when an order is created (auto_now_add=True).
#total_amount: A decimal field to store the total amount of the order.
#__str__() method provides a more informative representation of an Order object.