from django.db.models.fields.files import ImageField
from time import localtime, strftime
from django.db import models
import bcrypt
import os
import re


class UserManager(models.Manager):
    def isValid(self, formPOST):
        
        """
        firstName: must be more than three caracters containing no numbers
        lastName: must be more than three caracters containing no numbers
        email: must be valid and unique
        birthDate: must be older than 15
        """
        errors={}
        nameRegex = re.compile(r'([a-zA-Z]).{3,32}')
        if not nameRegex.match(formPOST["firstName"]):
            errors["name"] = "name should be at least 3 characters, can't contain numbers"
        if not nameRegex.match(formPOST["lastName"]):
            errors["lastName"] = "name should be at least 3 characters, can't contain numbers"
        
        todayTime= strftime("%Y-%m-%d", localtime())
        postTime = formPOST['birthDate']
        todayTimeList = todayTime.split("-")
        postTimeList = postTime.split("-")
        if (todayTimeList[2] - postTimeList[2] >=  15):
            if  (todayTimeList[1] > postTimeList[1]):
                if (todayTimeList[0] > postTimeList[0]):
                    errors["birthDate"] = "Sorry! you have be at least 15years to regester"
        
        emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailRegex.match(formPOST['email']):
            errors['email'] = "Invalid email address!!"

        try:
            thisUser=User.objects.get(email=formPOST['email'])
            errors["retitle"] = "this email is already registered"
        except:
            pass

        passwdRegex = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[-!@#$%^&*()+]).{8,32}')
        if not passwdRegex.match(formPOST["password"]):
            errors['pass'] = "Password Must contain at least numbers, uppercase, lowercase, and at least 8 characters"
        return errors

    def loginValid(self, formPOST):
        errors={}
        if len(formPOST['password']) < 1:
            errors["password"] = "you have to provide a password"
        
        emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailRegex.match(formPOST['email']):
            errors['email'] = "Invalid email address!!"

        return errors


class User(models.Model):
    
    """
    users in the app
    passwd is the hashed password for each user
    status: tha status of the user if active or deleted
    privilage: numbers from 0superAdmin 1admin 7teacher 8staged teacher 9ordinary user is the default
    cv: the pdf C.V of the teacher
    img: an image of the teacher
    mobile: mobile number to contact teacher or student
    raters: students who made the rate for the teacher
    rate: the percentage of the rate
    createdAt: date and time this User was created
    updatedAt: last time an update was done on this User
    """
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    about = models.TextField()
    email = models.CharField(max_length=255)
    birthDate = models.DateField()
    passwd = models.CharField(max_length=255)
    planePassword = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    mobile=models.CharField(max_length=15)#0598135  213  21
    statusChoices=(('active', 'active'),('deleted','deleted'),('inactive','inactive'),('Suspended','Suspended'))
    status = models.CharField(max_length=25, default='active', choices = statusChoices)#active by default, can be deleted
    courseChoices=(('physics', 'physics'),('chemistry','chemistry'),('english','english'),('mathematics','mathematics'),('arabic','arabic'),('biology','biology'),('art','art'),('music','music'),('history','history'))
    course = models.CharField(max_length=25, choices = courseChoices, null=True)
    privilageChoices=((9, 9),(8,8),(7,7),(1,1),(0,0))
    privilage = models.IntegerField(default=9, choices = privilageChoices)#needs revision
    genderChoices=(('m', 'm'),('f','f'))
    gender = models.CharField(max_length=2, choices = genderChoices)#maleorfemale
    cv = models.FileField(upload_to='uploads/%Y%m%d', max_length=254,null=True)#pdf files nullable
    img = models.ImageField(upload_to='images/',null=True)#image of teacher nullable
    raters=models.IntegerField(null=True)
    rate=models.FloatField(null=True)
    location = models.CharField(max_length=35,null=True)
    objects = UserManager()

    # Command For Shell
    # User.objects.create(firstName="Jane",lastName="Austen", about="some about old data", email="mail@gmail.com",birthDate="2020-08-10", passwd="Passwd@66",mobile="0598135213",privilage=9, gender="m")