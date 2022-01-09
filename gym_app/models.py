from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(max_length=100)
    equipment_price = models.DecimalField(decimal_places=2, max_digits=15)
    acquisition_date = models.DateField()
    last_maintenance = models.DateField()
    next_maintenance = models.DateField()
    equipment_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.equipment_name

class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    subscription_name = models.CharField(max_length=30)
    subscription_duration = models.CharField(max_length=50)
    subscription_price = models.DecimalField(decimal_places=2, max_digits=15)

    def __str__(self):
        return self.subscription_name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_phone_number = models.IntegerField()
    customer_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_subscription_id = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    customer_subscription_date = models.DateTimeField()
    customer_subscription_expiry_date = models.DateTimeField()

    def __str__(self):
        return self.customer_name


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_transaction_id = models.CharField(max_length=50)
    payment_amount = models.DecimalField(decimal_places=2, max_digits=15)
    payment_customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.payment_transaction_id

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    workout_name = models.CharField(max_length=30)
    workout_description = models.TextField()
    workout_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.workout_name

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=30)
    event_description = models.TextField()
    event_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name
