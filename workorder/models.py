from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError

from django.urls import reverse

from product.models import Product
from routing.models import Routing

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

class WorkOrder(models.Model):
	name 				= models.CharField(max_length=50,primary_key=True)
	title 				= models.CharField(max_length=100,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	product 			= models.ForeignKey(Product)
	routing 			= models.ForeignKey(Routing,blank=True, null=True)
	qty 				= models.IntegerField(default=0)
	regexp 				= models.CharField(verbose_name='RegExp Validation',max_length=100,blank=True, null=True,default='*')
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	finished_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('workorder:detail', kwargs={'slug': self.slug})

def create_workorder_slug(instance, new_slug=None):
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = WorkOrder.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_workorder_slug(instance, new_slug=new_slug)
    return slug

def pre_save_workorder_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_workorder_slug(instance)

pre_save.connect(pre_save_workorder_receiver, sender=WorkOrder)