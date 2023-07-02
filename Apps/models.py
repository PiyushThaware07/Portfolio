from django.db import models

# Create your models here.
class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    degree =  models.CharField(max_length=100, null=False)
    fieldofstudy = models.CharField(max_length=256,null=False)
    institutionname = models.CharField(max_length=256,null=False)
    startyear = models.IntegerField(null=True)
    endyear = models.IntegerField(null=True)
    def __str__(self):
        return self.degree


class Experience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    jobtitle = models.CharField(max_length=256,null=False)
    companyname = models.CharField(max_length=256,null=False)
    location = models.CharField(max_length=256,null=False)
    description = models.TextField()
    fromdate = models.DateField(blank=True,auto_now=False)
    todate = models.DateField(blank=True, auto_now=False)
    iscurrentjob = models.BooleanField(default=False)
    def __str__(self):
        return self.jobtitle
