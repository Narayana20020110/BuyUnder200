from django.contrib import admin
from .models import Product, Customer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)
    fields=('name','image','price')
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'product', 'delivery')
    list_filter = ('delivery',)
    search_fields = ('name', 'mobile', 'product__name')
    actions = ['mark_as_delivered']

    @admin.action(description="Mark selected orders as delivered")
    def mark_as_delivered(self, request, queryset):
        queryset.update(delivery=True)


    