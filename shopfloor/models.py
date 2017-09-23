from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError

# Create your models here.
ACTIVE='A'
DEACTIVE='D'
STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEACTIVE, 'Deactive'),
    )

# Master data Model
class Bom(models.Model):
	name = models.CharField(max_length=50,primary_key=True)
	title = models.CharField(max_length=100,blank=True, null=True)
	slug = models.SlugField(unique=True,blank=True, null=True)
	description = models.TextField(max_length=255,blank=True, null=True)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return self.name

	def item_count(self):
		return self.parts.count()

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

class BomDetail(models.Model):
	rd = models.CharField(verbose_name ='Ref Destinator',max_length=50)
	pn = models.CharField(verbose_name ='Part Number',max_length=50)
	bom = models.ForeignKey('Bom', related_name='parts')
	slug = models.SlugField(unique=True,blank=True, null=True)
	description = models.TextField(max_length=255,blank=True, null=True)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	customer_pn = models.CharField(max_length=50,blank=True, null=True)
	alt_pn = models.IntegerField(default=0,verbose_name ='Alternative Part')
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return ('%s : %s' % (self.rd,self.pn))

	class Meta:
		unique_together = ('rd','pn','bom','alt_pn')

def create_bomdetail_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s-%s-%s' % (instance.bom,instance.pn,instance.rd,instance.alt_pn)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = BomDetail.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_bomdetail_slug(instance, new_slug=new_slug)
    return slug

def pre_save_bomdetail_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_bomdetail_slug(instance)

pre_save.connect(pre_save_bomdetail_receiver, sender=BomDetail)

class Operation(models.Model):
	name = models.CharField(max_length=50,primary_key=True)
	title = models.CharField(max_length=100,blank=True, null=True)
	slug = models.SlugField(unique=True,blank=True, null=True)
	description = models.TextField(max_length=255,blank=True, null=True)
	customer_name = models.CharField(max_length=50,blank=True, null=True)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return ('%s : %s' % (self.name,self.title))

def create_operation_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_operation_slug(instance, new_slug=new_slug)
    return slug

def pre_save_operation_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_operation_slug(instance)

pre_save.connect(pre_save_operation_receiver, sender=Operation)

# Routing Configuration
class Routing(models.Model):
	name = models.CharField(max_length=50,primary_key=True)
	title = models.CharField(max_length=100,blank=True, null=True)
	slug = models.SlugField(unique=True,blank=True, null=True)
	description = models.TextField(max_length=255,blank=True, null=True)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return self.name

def create_routing_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_routing_slug(instance, new_slug=new_slug)
    return slug

def pre_save_routing_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routing_slug(instance)

pre_save.connect(pre_save_routing_receiver, sender=Routing)

class RoutingDetail(models.Model):
	FIRST='F'
	LAST='L'
	NORMAL = 'N'
	OPERATION_POS_CHOICES = (
	        (FIRST, 'First Operation'),
	        (LAST, 'Last Operation'),
	        (NORMAL, 'Normal'),
	    )
	operation = models.ForeignKey('Operation', related_name='routings',blank=True, null=True)
	routing = models.ForeignKey('Routing', related_name='operations')
	slug = models.SlugField(unique=True,blank=True, null=True)
	position = models.CharField(max_length=1,choices=OPERATION_POS_CHOICES,default=NORMAL)
	description = models.TextField(max_length=255,blank=True, null=True)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	next_pass = models.ForeignKey('Operation', related_name='nextpass')
	next_fail = models.ForeignKey('Operation', related_name='nextfail')
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return ('%s on %s' % (self.operation,self.routing))

def create_routingdetail_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.operation,instance.routing)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_routingdetail_slug(instance, new_slug=new_slug)
    return slug

def pre_save_routingdetail_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_routingdetail_slug(instance)

pre_save.connect(pre_save_routingdetail_receiver, sender=RoutingDetail)


class Product(models.Model):
	name = models.CharField(max_length=50,primary_key=True)
	title = models.CharField(max_length=100,blank=True, null=True)
	pn  = models.CharField(max_length=50,blank=True, null=True)
	rev  = models.CharField(max_length=50,blank=True, null=True)
	slug = models.SlugField(unique=True,blank=True, null=True)
	routing = models.ForeignKey('Routing', related_name='products',blank=True, null=True)
	description = models.TextField(max_length=255,blank=True, null=True)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	customer_pn = models.CharField(max_length=50,blank=True, null=True)
	customer_rev  = models.CharField(max_length=50,blank=True, null=True)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return self.name

def create_product_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s' % (instance.name)
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_product_slug(instance, new_slug=new_slug)
    return slug

def pre_save_product_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_product_slug(instance)

pre_save.connect(pre_save_product_receiver, sender=Product)




class WorkOrder(models.Model):
	name = models.CharField(max_length=50,primary_key=True)
	title = models.CharField(max_length=100,blank=True, null=True)
	description = models.TextField(max_length=255,blank=True, null=True)
	slug = models.SlugField(unique=True,blank=True, null=True)
	product = models.ForeignKey('Product', related_name='workorders')
	routing = models.ForeignKey('Routing', related_name='workorders',blank=True, null=True)
	qty = models.IntegerField(default=0)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	finished_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return self.name

def create_workorder_slug(instance, new_slug=None):
    # import datetime
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

class SerialNumber(models.Model):
	number = models.CharField(max_length=100)
	workorder = models.ForeignKey('WorkOrder', related_name='units')
	slug = models.SlugField(unique=True,blank=True, null=True)
	description = models.TextField(max_length=255,blank=True, null=True)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	registered_date = models.DateTimeField(auto_now_add=True)
	routing = models.ForeignKey('Routing', related_name='serialnumbers',blank=True, null=True)
	current_operation = models.ForeignKey('Operation', related_name='onprocess',blank=True, null=True)
	last_operation = models.ForeignKey('Operation', related_name='justpass',blank=True, null=True)
	last_modified_date = models.DateTimeField(blank=True, null=True)
	last_result = models.BooleanField(verbose_name = 'Last Result',default=False)
	finished_date = models.DateTimeField(blank=True, null=True)
	wip = models.BooleanField(verbose_name = 'Work In Process',default=True)
	perform_start_date = models.DateTimeField(blank=True, null=True)
	perform_operation = models.ForeignKey('Operation', related_name='onperform',blank=True, null=True)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return ('%s on %s' % (self.number,self.workorder))

	class Meta:
		unique_together = ('number','workorder')

def create_serialnumber_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.number,instance.workorder )
    slug = slugify(default_slug)
    if new_slug is not None:
        slug = new_slug
    qs = SerialNumber.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_serialnumber_slug(instance, new_slug=new_slug)
    return slug

def pre_save_serialnumber_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_serialnumber_slug(instance)

pre_save.connect(pre_save_serialnumber_receiver, sender=SerialNumber)


class Performing(models.Model):
	sn = models.ForeignKey('SerialNumber', related_name='performings')
	operation = models.ForeignKey('Operation', related_name='perform_units')
	slug = models.SlugField(unique=True,blank=True, null=True)
	start_time = models.DateTimeField(blank=True, null=True)
	stop_time = models.DateTimeField(blank=True, null=True)
	result = models.BooleanField(default=False)
	remark = models.TextField(max_length=255,blank=True, null=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return ('%s on %s' % (self.sn,self.operation))

def create_performing_slug(instance, new_slug=None):
    # import datetime
    default_slug = '%s-%s' % (instance.sn,instance.operation )
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

