from django.contrib import admin

from goods.models import Categories, Products


# admin.site.register(Categories)
# admin.site.register(Products)



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price', 'discount', 'ingridients']
    list_editable = ['discount']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'category']
    fields = ['name', 'category', 'slug', 'description', 'ingridients', ('price', 'discount')]