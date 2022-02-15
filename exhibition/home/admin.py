import django
from django.contrib import admin
from home.models import Profile,Category,Product, Comment, Bid
# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Bid)


