from django.contrib import admin
from .models import *

admin.site.register(Dishes)
admin.site.register(Tag)
admin.site.register(Customer)
admin.site.register(Order)