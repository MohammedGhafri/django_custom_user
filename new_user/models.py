from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# Create your models here.





#----------------------------------#


from django.contrib.auth.base_user import BaseUserManager
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


#---------------------#




class CustomUser(AbstractUser):

    desired_field = 'email address' # can be edited to what you want, But make Sure its compatibale with other instructions


    email = models.EmailField(_(desired_field), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # To ensure all fields are required

    objects = CustomUserManager()
    # add additional fields in here

    def __str__(self):
        return self.username
