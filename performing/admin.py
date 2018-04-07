from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from performing.models import Performing

admin.site.register(Performing)