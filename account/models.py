from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,  PermissionsMixin
# from django.contrib.auth.models import MyUser

class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("Email is required")
        
        if not full_name:
            raise ValueError("Full Name is required")
        
        
        user=self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, full_name,  password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            password=password,
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(verbose_name="Full Name", max_length=200, unique=True)
    email = models.EmailField(verbose_name="Email Address", max_length=60, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date Joined")
    last_login = models.DateTimeField(verbose_name="last_login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['full_name']

    objects=MyUserManager()

    def __str__(self):
        return self.full_name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    


class Profile(models.Model):
    is_active = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='', upload_to='Profile_images')

    def __str__(self):
        return f'{self.is_active.full_name}'
