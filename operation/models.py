from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError


ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

class Operation(models.Model):
	name 				= models.CharField(max_length=50,primary_key=True)
	customer_name  		= models.CharField(max_length=50,blank=True, null=True)
	title 				= models.CharField(max_length=100,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	customer_name 		= models.CharField(max_length=50,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return ('%s : %s' % (self.name,self.title))

	def get_absolute_url(self):
		return reverse('operation:detail', kwargs={'slug': self.slug})


def create_operation_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Operation.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_operation_slug(instance, new_slug=new_slug)
    return slug

def pre_save_operation_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_operation_slug(instance)

pre_save.connect(pre_save_operation_receiver, sender=Operation)