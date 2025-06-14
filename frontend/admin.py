from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Category, Product

class CustomUserAdmin(UserAdmin):
    # Fields to display in the user list in admin
    list_display = ('username', 'email', 'phone_number', 'is_staff', 'is_active')
    
    # Fields to add to the user creation form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address',)}),
    )
    
    # Fields to display in the user change form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at' # Adds navigation by date for created_at
    ordering = ('name',)
    
    # Prepopulate slug field if you were to add one based on name
    # prepopulated_fields = {'slug': ('name',)} 
