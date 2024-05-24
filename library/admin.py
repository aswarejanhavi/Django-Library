from django.contrib import admin

# Register your models here.
# Username (leave blank to use 'dell'): PraisElite
# Email address: praiselite@gmail.com
# password :I-X

from .models import Book,Borrower

admin.site.register(Book)
admin.site.register(Borrower)