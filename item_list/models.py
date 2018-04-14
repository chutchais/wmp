from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from item.models import Item
from django.conf import settings

ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

class ItemList(models.Model):
	name 			= models.CharField(max_length=50)
	value 			= models.CharField(max_length=50)
	title 			= models.CharField(max_length=100,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	default 		= models.BooleanField(default=False)
	item 			= models.ForeignKey(Item,
						on_delete=models.CASCADE,)
	ordered 		= models.IntegerField(default=1)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	def __str__(self):
		return ('%s of %s' % (self.name,self.item))

	def get_absolute_url(self):
		return reverse('item-list:detail', kwargs={'slug': self.slug})

def create_itemlist_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.name,instance.item )
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = ItemList.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_itemlist_slug(instance, new_slug=new_slug)
    return slug

def pre_save_itemlist_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_itemlist_slug(instance)

pre_save.connect(pre_save_itemlist_receiver, sender=ItemList)