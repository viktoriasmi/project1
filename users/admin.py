from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabularAdmin
from orders.models import Order, OrderItem
from users.models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'email']
    search_fields = ['username', 'last_name', 'first_name', 'email']

    inlines = [CartTabAdmin, OrderTabularAdmin]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        if not change:
            orders_formset = [
                formset for formset in formsets if formset.model == Order
            ][0]
            for order_form in orders_formset:
                if order_form.instance.pk:
                    if not OrderItem.objects.filter(order=order_form.instance).exists():
                        order_form.instance.delete()
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj: 
            if 'created_timestamp' in form.base_fields:
                form.base_fields['created_timestamp'].disabled = True
        return form
    
    def save_model(self, request, obj, form, change):
        if not change:
            password = form.cleaned_data.get('password')
            if password:
                obj.set_password(password)  
        super().save_model(request, obj, form, change)
