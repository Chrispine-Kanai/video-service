from django.contrib import admin
from .models import Membership, UserMembership, Subscription


# Register your models here.
admin.register(Membership, UserMembership, Subscription)
