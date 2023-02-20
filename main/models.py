from django.db import models

# Create your models here.

class Project(models.Model):
	title= models.CharField(max_length=50, null=True, blank=True)
	category = models.CharField(max_length=200, null=True, blank=True)
	project_url = models.CharField(max_length=200, null=True, blank=True)
	client = models.CharField(max_length=50, null=True, blank=True)
	project_description= models.TextField(null=True, blank=True)
	summary= models.TextField(null=True, blank=True)
	idea= models.TextField(null=True, blank=True)
	research= models.TextField(null=True, blank=True)
	launch= models.TextField(null=True, blank=True)
	result= models.TextField(null=True, blank=True)
	project_first_pic = models.ImageField(null=True, blank=True, upload_to="projects")
	project_second_pic = models.ImageField(null=True, blank=True, upload_to="projects")
	project_third_pic = models.ImageField(null=True, blank=True, upload_to="projects")
	def __str__(self):
		return self.title


class Contact(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(blank=True, null=True)
	phone = models.CharField(max_length=11, blank=True, null=True)
	subject = models.CharField(max_length=200, null=True, blank=True)
	message = models.TextField(blank=True, null=True)

class Info(models.Model):
	email = models.EmailField(blank=True, null=True)
	phone_no= models.CharField(max_length=11,blank=True, null=True)
	fb_link = models.CharField(max_length=200, blank=True, null=True)
	twitter_link = models.CharField(max_length=200, blank=True, null=True)
	instagram_link = models.CharField(max_length=200, blank=True, null=True)
	linkedin_link = models.CharField(max_length=200, blank=True, null=True)
	github_link = models.CharField(max_length=200, blank=True, null=True)
	resume = models.FileField(upload_to='resume/', default=None, null=True, help_text='Enter Your resume here')
