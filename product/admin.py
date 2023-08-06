from django.contrib import admin
from product.models import *


@admin.register(Product_category)
class Product_categoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'created_at', 'modified_at']


@admin.register(Product_inventory)
class Product_inventoryAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'created_at', 'modified_at']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'discount_percent', 'active', 'created_at', 'modified_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'sku', 'category', 'inventory', 'price', 'discount', 'created_at', 'modified_at']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'first_name', 'last_name', 'mobile', 'created_at', 'modified_at']


@admin.register(Payment_details)
class Payment_detailsAdmin(admin.ModelAdmin):
    list_display = ['order', 'amount', 'provider', 'status', 'created_at', 'modified_at']


@admin.register(User_address)
class User_addressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address1', 'address2', 'city', 'postal_code', 'country', 'telephone', 'mobile']


@admin.register(User_payment)
class User_paymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_type', 'provider', 'account_no', 'expiry']


@admin.register(Order_details)
class Orde_detailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'total', 'payment', 'created_at', 'modified_at']


@admin.register(Order_items)
class Order_itemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'created_at', 'modified_at']


@admin.register(shopping_session)
class shopping_sessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'total', 'created_at', 'modified_at']


@admin.register(Cart_item)
class Cart_itemAdmin(admin.ModelAdmin):
    list_display = ['session', 'product', 'quantity', 'created_at', 'modified_at']

