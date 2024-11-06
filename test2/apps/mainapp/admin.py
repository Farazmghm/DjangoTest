# 
from django.contrib import admin
from .models import Faraz, Company, Product_company, Emplyee

@admin.register(Faraz)
class farazAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'email', 'register')
    list_filter = ('family',)
    search_fields = ('family',)
    ordering = ['family', 'name']

@admin.register(Company)
class companyAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'member', 'product')

@admin.register(Product_company)
class productAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'production_date', 'produst_price')
    list_filter = ('product_id',)  # به صورت لیست یا تاپل
    search_fields = ('product_id', 'product_name')
    ordering = ['product_id']

@admin.register(Emplyee)
class employeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'family', 'address', 'email', 'number', 'is_active', 'slug')
    list_filter = ('employee_id', 'family')
    search_fields = ('employee_id', 'family', 'name')
    ordering = ['family', 'name']
    prepopulated_fields = {'slug': ('name', 'family')}



