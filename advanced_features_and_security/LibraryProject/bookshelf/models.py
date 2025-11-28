from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# -------------------------------
# Book model
# -------------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"


# -------------------------------
# Custom User Manager
# -------------------------------
class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser with additional fields like date_of_birth and profile_photo.
    """

    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and save a regular user with the given username, email, password, date_of_birth, and profile_photo.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and save a superuser with the given username, email, password, date_of_birth, and profile_photo.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, date_of_birth, profile_photo, **extra_fields)


# -------------------------------
# Custom User model
# -------------------------------
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()  # Attach the custom manager

    def __str__(self):
        return self.username
