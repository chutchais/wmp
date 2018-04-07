from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse

from serialnumber.models import SerialNumber
from operation.models import Operation

class Performing(models.Model):
	sn 				= models.ForeignKey(SerialNumber, related_name='performings')
	operation 		= models.ForeignKey(Operation, related_name='perform_units')
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	start_time 		= models.DateTimeField(blank=True, null=True)
	stop_time 		= models.DateTimeField(blank=True, null=True)
	result 			= models.BooleanField(default=False)
	remark 			= models.TextField(max_length=255,blank=True, null=True)
	user 			= models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return ('%s on %s' % (self.sn,self.operation))

	def get_absolute_url(self):
		return reverse('performing:detail', kwargs={'slug': self.slug})

def create_performing_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.sn.number,instance.operation.name )
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Performing.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_performing_slug(instance, new_slug=new_slug)
    return slug

def pre_save_performing_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_performing_slug(instance)

pre_save.connect(pre_save_performing_receiver, sender=Performing)