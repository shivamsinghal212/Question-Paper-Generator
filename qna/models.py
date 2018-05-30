from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Teacher(models.Model):
    pass


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    dob = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.student.save()


class Questions(models.Model):
    SUBJECT_LIST = (('Science','Science'),('Mathematics','Mathematics'),('Social-Studies','Social-Studies'),
                    ('English','English'),('Moral-Science','Moral-Science'))
    KLASS_LIST = (('1st','I'),('2nd','II'),('3rd','III'),('4th','IV'),('5th','V'),('6th','VI'),
                    ('7th','VII'),('8th','VIII'))
    QUESTION_TYPE = (('TR','Teacher'),('BK','Book'))
    qtype = models.CharField(max_length = 100, choices = QUESTION_TYPE)
    question = models.CharField(max_length = 300, unique = True)
    subject = models.CharField(max_length = 50, choices = SUBJECT_LIST)
    klass = models.CharField(max_length=10, choices = KLASS_LIST)
    answer = models.CharField(max_length = 2000)

    def __str__(self):
        return self.question


class Questionpaper(models.Model):
    paperid = models.CharField(max_length = 5, unique = True)
    papername = models.CharField(max_length = 25)
    subject  = models.CharField(max_length = 50)
    klass = models.CharField(max_length = 10)
    questions = models.ManyToManyField(Questions)

    def __str__(self):
        return self.papername
