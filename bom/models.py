from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings


ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

class Bom(models.Model):
	name 			= models.CharField(max_length=50,primary_key=True)
	pn 				= models.CharField(verbose_name ='Part Number',max_length=50,blank=True, null=True)
	rev 			= models.CharField(verbose_name ='Revision',max_length=10,blank=True, null=True)
	title 			= models.CharField(max_length=100,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	description 	= models.TextField(blank=True, null=True)
	customer_pn 	= models.CharField(verbose_name ='Customer Part Number',max_length=50,blank=True, null=True)
	customer_rev 	= models.CharField(verbose_name ='Customer Revision',max_length=10,blank=True, null=True)
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('bom:detail', kwargs={'slug': self.slug})

	def item_count(self):
		return self.bom_detail_set.count()

def create_bom_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Bom.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_bom_slug(instance, new_slug=new_slug)
    return slug

def pre_save_bom_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_bom_slug(instance)

pre_save.connect(pre_save_bom_receiver, sender=Bom)