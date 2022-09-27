
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

########## Custom Model manager ########

class CustomUserManager(BaseUserManager):
    def create_user(self ,username, email  , phone_number, password, image):
        
        if not email:
            raise ValueError('The Email must be Set')
        if not username:
            raise ValueError("User Must have a username ")  

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phone_number = phone_number,
            image = image
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username,phone_number,password,image):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            
            
            
            phone_number = phone_number,
            image = image,
            password = password,
           
      
        )
     
        user.is_admin = True
        user.is_superuser = True
       
        user.save(using = self._db)
        return user    

############ Custom User Model ###########
class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(verbose_name = 'Email',max_length=255,unique=True)
    image = models.FileField(default="buildingimages/default.png", blank=True)
    phone_number = models.CharField(max_length = 15, unique=True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_number', 'image']

    def __str__(self):
      return self.email

    def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

    def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

    @property
    def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin


# def Event():
#     pass         