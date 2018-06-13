from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings

from performing.models import Performing
from parameter.models import Parameter

class Parametric(models.Model):
	performing		= models.ForeignKey(Performing,
						on_delete=models.CASCADE,)
	parameter 		= models.ForeignKey(Parameter,
						on_delete=models.CASCADE,)
	value 			= models.TextField(max_length=255,blank=True, null=True)
	created_date 	= models.DateTimeField(auto_now_add=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL,
						on_delete=models.SET_NULL,
						blank=True,null=True)

	def __str__(self):
		return ('%s' % (self.parameter))

	def get_absolute_url(self):
		return reverse('parametric:detail', kwargs={'pk': self.pk})

