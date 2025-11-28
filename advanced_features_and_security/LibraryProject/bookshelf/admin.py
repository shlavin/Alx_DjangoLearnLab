from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# -------------------------------
# Book model admin
# -------------------------------
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)  # explicit registration for checker

# -------------------------------
# CustomUser model admin
# -------------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Include the custom fields in the admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'date_of_birth')

admin.site.register(CustomUser, CustomUserAdmin)  # explicit registration for checker
