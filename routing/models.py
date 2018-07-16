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

class Routing(models.Model):
	name 			= models.CharField(max_length=50,primary_key=True)
	title 			= models.CharField(max_length=100,blank=True, null=True)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	description 	= models.TextField(max_length=255,blank=True, null=True)
	category1 		= models.CharField(max_length=50,blank=True, null=True)
	category2 		= models.CharField(max_length=50,blank=True, null=True)
	status 			= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,blank=True,null=True)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('routing:detail', kwargs={'slug': self.slug})

def create_routing_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Routing.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_routing_slug(instance, new_slug=new_slug)
    return slug

def pre_save_routing_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routing_slug(instance)

pre_save.connect(pre_save_routing_receiver, sender=Routing)


# Routing Next
from snippet.models import Snippet

class RoutingDetailNext(models.Model):
	name 				= models.CharField(max_length=100)
	title 				= models.CharField(max_length=100,blank=True, null=True)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	snippet 			= models.ForeignKey(
					        Snippet,
					        on_delete=models.CASCADE,
					        related_name='routing_next',blank=True, null=True
					    )
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.SET_NULL,
							blank=True,null=True)

	def __str__(self):
		return ('%s' % (self.name))

	def get_absolute_url(self):
		return reverse('routing-next:detail', kwargs={'slug': self.slug})

def create_routingnext_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = RoutingNext.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_routingnext_slug(instance, new_slug=new_slug)
    return slug


def pre_save_routingnext_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routingnext_slug(instance)

pre_save.connect(pre_save_routingnext_receiver, sender=RoutingDetailNext)


# Routing Details
from operation.models import Operation
from parameter.models import Parameter
from routing_accept.models import RoutingAccept
from routing_reject.models import RoutingReject
# from routing.models import RoutingNext

class RoutingDetail(models.Model):
	FIRST='F'
	LAST='L'
	NORMAL = 'N'
	OPERATION_POS_CHOICES = (
			(FIRST, 'First Operation'),
			(LAST, 'Last Operation'),
			(NORMAL, 'Normal'),
		)
	operation 			= models.ForeignKey(Operation,
								on_delete=models.CASCADE,
								blank=True, null=True,
								related_name = 'routings')
	routing 			= models.ForeignKey(Routing,
								on_delete=models.CASCADE,
								related_name = 'details')
	title 				= models.CharField(max_length=100,blank=True, null=True)
	slug 				= models.SlugField(unique=True,blank=True, null=True)
	position 			= models.CharField(max_length=1,choices=OPERATION_POS_CHOICES,default=NORMAL)
	description 		= models.TextField(max_length=255,blank=True, null=True)
	category1 			= models.CharField(max_length=50,blank=True, null=True)
	category2 			= models.CharField(max_length=50,blank=True, null=True)
	next_pass 			= models.ForeignKey(Operation,
								related_name='nextpasses',
								on_delete=models.SET_NULL,blank=True, null=True)
	next_fail 			= models.ForeignKey(Operation,
								related_name='nextfails',
								on_delete=models.SET_NULL,blank=True, null=True)
	parameter 			= models.ManyToManyField(Parameter, through='RoutingDetailParameterSet')
	accept_code 		= models.ManyToManyField(RoutingAccept, through='RoutingDetailAcceptSet')
	reject_code 		= models.ManyToManyField(RoutingReject, through='RoutingDetailRejectSet')
	next_code 			= models.ManyToManyField(RoutingDetailNext, through='RoutingDetailNextSet')
	status 				= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 		= models.DateTimeField(auto_now_add=True)
	modified_date 		= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.SET_NULL,
								blank=True,null=True)
	
	def __str__(self):
		return ('%s on %s' % (self.operation,self.routing))

	def get_absolute_url(self):
		return reverse('routing-detail:detail', kwargs={'slug': self.slug})

def create_routingdetail_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.operation,instance.routing)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = RoutingDetail.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_routingdetail_slug(instance, new_slug=new_slug)
    return slug

def pre_save_routingdetail_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routingdetail_slug(instance)

pre_save.connect(pre_save_routingdetail_receiver, sender=RoutingDetail)


class RoutingDetailParameterSet(models.Model):
	routingdetail 			= models.ForeignKey('RoutingDetail', on_delete=models.CASCADE)
	parameter 				= models.ForeignKey(Parameter, on_delete=models.CASCADE)
	ordered 				= models.IntegerField(default=1)
	required 				= models.BooleanField(default=False)
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.SET_NULL,
								blank=True,null=True)

	def __str__(self):
		return ('%s of %s' % (self.parameter,self.routingdetail))


class RoutingDetailAcceptSet(models.Model):
	routingdetail 			= models.ForeignKey('RoutingDetail', on_delete=models.CASCADE)
	routingaccept 			= models.ForeignKey(RoutingAccept, on_delete=models.CASCADE)
	ordered 				= models.IntegerField(default=1)
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.SET_NULL,
								blank=True,null=True)

	def __str__(self):
		return ('%s of %s' % (self.routingaccept,self.routingdetail))


class RoutingDetailRejectSet(models.Model):
	routingdetail 			= models.ForeignKey('RoutingDetail', on_delete=models.CASCADE)
	routingreject 			= models.ForeignKey(RoutingReject, on_delete=models.CASCADE)
	ordered 				= models.IntegerField(default=1)
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
									on_delete=models.SET_NULL,
									blank=True,null=True)

	def __str__(self):
		return ('%s of %s' % (self.routingreject,self.routingdetail))


class RoutingDetailNextSet(models.Model):
	routingdetail 			= models.ForeignKey('RoutingDetail',
									related_name='nexts', 
									on_delete=models.CASCADE)
	routingnext 			= models.ForeignKey(RoutingDetailNext, 
									related_name='nexts',
									on_delete=models.CASCADE)
	title 					= models.CharField(max_length=100,blank=True, null=True)
	ordered 				= models.IntegerField(default=1)
	operation 				= models.CharField(max_length=100,blank=True, null=True)# models.ForeignKey(Operation, related_name='routingdetailsets')
	status 					= models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date 			= models.DateTimeField(auto_now_add=True)
	modified_date 			= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 					= models.ForeignKey(settings.AUTH_USER_MODEL,
									on_delete=models.SET_NULL,
									blank=True,null=True)

	def __str__(self):
		return ('%s of %s' % (self.routingnext,self.routingdetail))


