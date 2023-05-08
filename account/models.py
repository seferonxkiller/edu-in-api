from django.db import models
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models.signals import post_save, pre_save


def image_path(instance, filename):
    return f"account/{instance.id}/{filename}"


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('User should have a email')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if password is None:
            raise TypeError('Password should not be None')

        user = self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.role = 2
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        (0, "Student"),
        (1, "Teacher"),
        (2, "Stuff"),
    )
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email', db_index=True)
    first_name = models.CharField(max_length=50, verbose_name='First name', null=True)
    last_name = models.CharField(max_length=50, verbose_name='Last name', null=True)
    image = models.ImageField(upload_to=image_path)
    role = models.IntegerField(choices=ROLE, default=0)
    bio = models.TextField()
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Date modified')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    objects = AccountManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.last_name} {self.first_name}'
        return f'{self.email}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:30px;"/></a>')
        else:
            return 'Image not found'


    @property
    def image_url(self):
        if self.image:
            if settings.DEBUG:
                return f'{settings.LOCAL_BASE_URL}{self.image.url}'
            return f'{settings.PROD_BASE_URL}{self.image.url}'
        return None

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data


def account_post_save(instance, sender, *args, **kwargs):
    if instance.role == 2:
        instance.is_staff = True
    else:
        instance.is_staff = False
    return instance


pre_save.connect(account_post_save, sender=Account)
