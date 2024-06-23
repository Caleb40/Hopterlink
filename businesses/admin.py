from django.contrib import admin

from businesses.models.business_model import Business
from businesses.models.category_model import Category
from businesses.models.category_model import Subcategory

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Business)
