from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class MyUserManager(BaseUserManager):
    def create_user(self, status, first_name,last_name, email, date_of_birth, sex, marriage_status, primary_contact, secondary_contact,
                    password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            status=status,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            specialization=specialization,
            sex=sex,
            first_name=first_name,
            last_name=last_name,
            marriage_status=marriage_status,
            primary_contact=primary_contact,
            secondary_contact=secondary_contact,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=20, unique=True)
    USERNAME_FIELD = 'identifier'
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True,)
    status=models.CharField(max_length=15, unique=False)
    is_active=models.BooleanField(default=True)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=10, unique=False)
    first_name = models.CharField(max_length=40, unique=False)
    last_name = models.CharField(max_length=40, unique=False)
    marriage_status = models.BooleanField(default=False)
    primary_contact = models.IntegerField(max_length=11)
    secondary_contact = models.IntegerField(max_length=11)
    is_admin = models.BooleanField(default=False)
	
    objects = MyUserManager()
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.name

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
class Patient(MyUser):
    is_content_manager=models.BooleanField(default=False)
    is_admin = False
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):                                              
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return False

    def save(self, *args, **kwargs):
        # if user being demoted from content manager, make sure they are not
        # managing any courses
        super().save(*args, **kwargs)
    
    
class Doctor(MyUser):
    is_content_manager=models.BooleanField(default=False)
    is_admin = False
    specialization= models.CharField(max_length=40, unique=False)
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):                                                 #idk on this one. probably not?
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):
        # if user being demoted from content manager, make sure they are not
        # managing any courses
        super().save(*args, **kwargs)

class Nurse(MyUser):
    is_content_manager=models.BooleanField(default=False)
    is_admin = False
    department= models.CharField(max_length=40, unique=False)
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):                                                 #idk on this one. probably not?
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):
        # if user being demoted from content manager, make sure they are not
        # managing any courses
        super().save(*args, **kwargs)
