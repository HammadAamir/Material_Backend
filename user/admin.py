from django.contrib import admin
from .models import User
# Register your models here.
from django.contrib.auth.models import Group

class RbacAuthUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_superuser', 'is_active']

    # def save_model(self, request, obj, form, change):
    #     if not change or 'password' in form.changed_data:
    #         obj.password = make_password(obj.password)
    #     super().save_model(request, obj, form, change)
admin.site.register(User, RbacAuthUserAdmin)
# admin.site.unregister(Group)