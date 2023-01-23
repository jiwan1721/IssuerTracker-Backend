from django.contrib import admin

from IssueTracker.views import User
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

# from .forms import MyUserCreationForm, MyUserChangeForm
from .models import Issue
# from .models import Issue


# class MyUserAdmin(UserAdmin):
#     add_form = MyUserCreationForm
#     form = MyUserChangeForm
#     model = User
#     list_display = ['username', 'mobile_number', 'birth_date']
#     fieldsets = UserAdmin.fieldsets + (
#             (None, {'fields': ('mobile_number', 'birth_date')}),
#     ) #this will allow to change these fields in admin module

admin.site.register(User)
admin.site.register(Issue)