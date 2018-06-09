from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings

from snippet.models import Snippet
from routing_detail.models import RoutingDetail

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

EVENT_CHOICES = (
        ('PRE', 'Pre-check'), #For Button at the beginning of Click event
        ('POST', 'Post-check'), #For Button at the end of Click event
        ('CLICK','Click-on'), #For Option,Radio and Combo list after Click or Selected event
        ('VALIDATE','Validate') #for Text lost focus event (once Failed , keep focus)
    )


class Hook(models.Model):
	name 			= models.CharField(max_length=100)#Local object name
	title 			= models.CharField(max_length=100,blank=True, null=True)
	description 	= models.TextField(max_length=255,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	ordered 		= models.IntegerField(default=1)
	event			= models.CharField(max_length=10,choices=EVENT_CHOICES,default='',blank=True, null=True)
	routing_detail	= models.ForeignKey(
					        RoutingDetail,
					        on_delete=models.CASCADE,
					        blank=True, null=True
					    )
	snippet 		= models.ForeignKey(
					        Snippet,
					        on_delete=models.CASCADE,
					        blank=True, null=True
					    )
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	def __str__(self):
		return ('%s' % (self.name))

	def get_absolute_url(self):
		return reverse('hook:detail', kwargs={'slug': self.slug})

def create_hook_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s-%s' % (instance.name,instance.event,instance.routing_detail)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Hook.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.count())
        return create_routingreject_slug(instance, new_slug=new_slug)
    return slug

def pre_save_hook_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_hook_slug(instance)

pre_save.connect(pre_save_hook_receiver, sender=Hook)




