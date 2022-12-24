from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from taggit.managers import TaggableManager



# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, fname, lname, gender , password=None , password2=None):
        """
        Creates and saves a User with the given email, name, 
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            fname = fname,
            lname = lname,
            gender = gender,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fname, lname, gender, password=None):
        """
        Creates and saves a superuser with the given email, name, tc  and password.
        """
        user = self.create_user(
            email,
            password=password,
            fname=fname,
            lname=lname,
            gender= gender,


            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom user model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )

    fname= models.CharField(max_length=200)
    lname=models.CharField(max_length=200)


    GENDER_CHOICES =(
        ('M','Male'),
        ('F','Female'),
    )
    gender=models.CharField(max_length=10, choices= GENDER_CHOICES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname', 'gender']

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


        # From here we add profile view

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to="static\images", default='static\images\pic1.jpg')
    bg_image = models.ImageField(upload_to="static\images", default='static\images\pic2.png')

    def __str__(self):
        return str(self.user)

def created_profile(sender, instance, created, **kwargs):
    if created:
        Profile .objects.create(user=instance)
        print("Profile Created")
post_save.connect(created_profile, sender=User) 

class PersonalInfo(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200)
    contact = models.IntegerField()
    dob = models.DateField(max_length=8)

    MARITAL_STATUS =(
        ('S','Singal'),
        ('M','Married'),
    )
    marital_status=models.CharField(max_length=10, choices= MARITAL_STATUS)
    address=models.CharField(max_length=500)

    def __str__(self):
        return str(self.fname)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    EDUCATION_CHOICE= (
        ('10th','SSC'),
        ('12th','HSC'),
        ('15th', 'Diploma'), 
    )
    education = models.CharField(max_length=50, choices = EDUCATION_CHOICE)
    board = models.CharField(max_length=100) 
    passing_Out_year = models.IntegerField()
    school_medium = models.CharField(max_length=100)
    total_marks = models.IntegerField()

    def __str__(self):
        return str(self.user)



class Experiance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100) 
    year_of_experiance = models.IntegerField()
    joining_date = models.DateField(max_length=8) 
    resigning_date = models.DateField(max_length=8) 
    job_role = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)


class Skills(models.Model):
    user = models.ManyToManyField(User)
    tags = TaggableManager()

    def __str__(self):
        return str(self.user)






    
