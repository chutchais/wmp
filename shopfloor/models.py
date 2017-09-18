from django.db import models

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

class BomDetail(models.Model):
	rd = models.CharField(max_length=50)
	pn = models.CharField(max_length=50)
	bom = models.ForeignKey('Bom', related_name='parts')
	slug = models.SlugField(unique=True,blank=True, null=True)
	description = models.TextField(max_length=255,blank=True, null=True)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	customer_pn = models.CharField(max_length=50,blank=True, null=True)
	alt_pn = models.IntegerField(default=0)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)
	
	def __str__(self):
		return ('%s : %s' % (self.rd,self.pn))

	class Meta:
		unique_together = ('rd','pn','bom','alt_pn')

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

class RoutingDetail(models.Model):
	FIRST='F'
	LAST='L'
	NORMAL = 'N'
	OPERATION_POS_CHOICES = (
	        (FIRST, 'First Operation'),
	        (LAST, 'Last Operation'),
	        (NORMAL, 'Normal'),
	    )
	operation = models.ForeignKey('Operation', related_name='routings')
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

class SerialNumber(models.Model):
	number = models.CharField(max_length=100)
	workorder = models.ForeignKey('WorkOrder', related_name='units')
	slug = models.SlugField(unique=True,blank=True, null=True)
	description = models.TextField(max_length=255,blank=True, null=True)
	category1 = models.CharField(max_length=50,blank=True, null=True)
	category2 = models.CharField(max_length=50,blank=True, null=True)
	registered_date = models.DateTimeField(auto_now_add=True)
	current_operation = models.ForeignKey('Operation', related_name='onprocess')
	last_operation = models.ForeignKey('Operation', related_name='justpass')
	last_modified_date = models.DateTimeField(blank=True, null=True)
	finished_date = models.DateTimeField(blank=True, null=True)
	wip = models.BooleanField(verbose_name = 'Work In Process',default=True)
	perform_start_date = models.DateTimeField(blank=True, null=True)
	perform_operation = models.ForeignKey('Operation', related_name='onperform',blank=True, null=True)
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=ACTIVE)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return ('%s on %s' % (self.number,self.workorder))


class Performing(models.Model):
	sn = models.ForeignKey('SerialNumber', related_name='performings')
	operation = models.ForeignKey('Operation', related_name='perform_units')
	start_time = models.DateTimeField(blank=True, null=True)
	stop_time = models.DateTimeField(blank=True, null=True)
	result = models.BooleanField(default=False)
	remark = models.TextField(max_length=255,blank=True, null=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return ('%s on %s' % (self.sn,self.operation))

	#All parameters - product,bom,WorkOrder,SerialNumber 

