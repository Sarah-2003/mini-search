from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender', 'location', 'phone_number', 'profile_photo', 'bio')

admin.site.register(User, UserAdmin)
