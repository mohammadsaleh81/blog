from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    is_author = models.BooleanField('نویسنده',default=False)
    special_user =models.DateTimeField('کاربر ویژه تا', default=timezone.now)
    email = models.EmailField('ایمیل',unique=True)


    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = 'وضعیت کاربر ویژه'