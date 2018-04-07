from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

from product.models import Product
from snippet.models import Snippet

class Item(models.Model):
	TEXTBOX ='TEXT'
	LIST ='LIST'
	RADIO ='RADIO'
	OPTION = 'OPTION'
	SCRIPT ='SCRIPT'
	PARAM_TYPE_CHOICES = (
	        (TEXTBOX, 'Text Box'),
	        (LIST, 'List Box'),
	        (RADIO, 'Radio Box'),
	        (OPTION, 'Option Box'),
	        (SCRIPT, 'Script Data'),
	    )
	name 				= models.CharField(max_length=50)
	title 				= models.CharField(max_length=100,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	product 			= models.ForeignKey(Product, related_name='parameters',blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	help_text 			= models.CharField(verbose_name='Help Text',max_length=100,blank=True, null=True)
	input_type 			= models.CharField(verbose_name='Input Type',max_length=10,choices=PARAM_TYPE_CHOICES,default=TEXTBOX)
	default_value 		= models.CharField(verbose_name='Default Value',max_length=100,blank=True, null=True)
	regexp 				= models.CharField(verbose_name='RegExp Validation',max_length=100,blank=True, null=True,default='\w')
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey('auth.User',blank=True,null=True)
	snippet 			= models.ForeignKey(Snippet, related_name='items',verbose_name='Snippet Code',blank=True, null=True)
	expected_return 	= models.CharField(verbose_name='Expected Return',default='TRUE',max_length=100,blank=True, null=True)

	# @property
	def has_validation_code(self):
		return True if (self.snippet) else False
	has_validation_code.boolean =True
	has_validation_code.short_description = 'Has Validation'

	def __str__(self):
		return ('%s : %s' % (self.name,self.input_type))

	def get_absolute_url(self):
		return reverse('item:detail', kwargs={'slug': self.slug})

def create_item_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.name,instance.input_type)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Item.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_item_slug(instance, new_slug=new_slug)
    return slug

def pre_save_item_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_item_slug(instance)

pre_save.connect(pre_save_item_receiver, sender=Item)