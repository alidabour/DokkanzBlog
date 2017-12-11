from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
	subject = models.CharField(max_length=200)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.subject

class Comment(models.Model):
	content = models.TextField()
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add= True)
	post_ref = models.ForeignKey(Post,on_delete=models.CASCADE)

	def __str__(self):
		return self.content