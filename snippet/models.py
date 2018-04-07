
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

class Snippet(models.Model):
	name 				= models.CharField(max_length=100)
	title 				= models.CharField(max_length=100,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	code 				= models.TextField()
	linenos 			= models.BooleanField(default=False)
	language 			= models.CharField(choices=LANGUAGE_CHOICES, default='VB.net', max_length=100)
	style 				= models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey('auth.User',blank=True,null=True)

	class Meta:
		ordering = ('created_date',)

	def __str__(self):
		return ('%s' % (self.name))

	def get_absolute_url(self):
		return reverse('snippet:detail', kwargs={'slug': self.slug})


def create_snippet_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Snippet.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_snippet_slug(instance, new_slug=new_slug)
    return slug

def pre_save_snippet_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_snippet_slug(instance)

pre_save.connect(pre_save_snippet_receiver, sender=Snippet)