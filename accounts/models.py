from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return self.name

tags = Tag.objects.all().values_list('name','name')
tag_list = []
for tag in tags:
	tag_list.append(tag)

class Dishes(models.Model):
	CATEGORY = (
		('rossa', 'rossa'),
		('pesto', 'pesto'),)

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	pic = models.ImageField(default="images/Quattro.jpg", null=True, blank=True)
	sause = models.CharField(max_length=200, null=True, choices=CATEGORY, blank=True)
	description = models.CharField(max_length=280, null=True, blank=True)
	tag = models.CharField(max_length=200, null=True, choices=tag_list)

	def __str__(self): 
		return f"{self.name} ─ {self.tag}"

	@property
	def imageURL(self):
		try:
			url = self.pic.url
		except:
			url = ''
		return url

class Order(models.Model):

	order_id = models.AutoField(auto_created=True,primary_key=True)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	order_date = models.DateTimeField(auto_now_add=True, null=True)
	complete = models.BooleanField(default=False, null=True, blank=False)

	def __str__(self):
		return f"Order no.{self.order_id} -by- {self.customer}"

	@property
	def get_cart_total(self):
		orderitems = self.orderitems_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitems_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItems(models.Model):
	order = models.ForeignKey(Order, on_delete = models.CASCADE) #related_name="orderitems",
	dishes = models.ForeignKey(Dishes, null=True, on_delete=models.SET_NULL)
	quantity = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.order} has {self.dishes} * {self.quantity}"
	
	@property
	def get_total(self):
		total = self.dishes.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	adress = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	zipcode = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
