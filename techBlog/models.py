from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length = 255)
	slug = models.SlugField(unique = True , max_length = 255 )
	description  =  models.CharField(max_length = 255)
	content = models.TextField()
	published = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add = True)
	views = models.IntegerField(default = 0)
	images = models.CharField(max_length = 255)
	likes = models.IntegerField(default= 0)
	publisher = models.CharField(max_length=255,default="Tushar Garg")
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('techBlog.views.post', args=[self.slug])
		
		