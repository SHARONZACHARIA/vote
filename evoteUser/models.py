from django.db import models
from django.contrib.auth.models import User


# Create your models here
class UserDetail(models.Model):
    phone = models.CharField(max_length=12)
    uid = models.CharField(max_length=12)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class VoteCase(models.Model) :
    username = models.TextField()
    vcid = models.TextField(primary_key=True)
    case_name = models.TextField()
    controller = models.TextField()
    desc = models.TextField()
    

class Candidates(models.Model):
    votecase = models.ForeignKey(VoteCase,on_delete=models.CASCADE)
    cname = models.TextField()
    desc= models.TextField()
    image=models.TextField() 
    count = models.CharField(max_length=5)
 