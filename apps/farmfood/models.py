from __future__ import unicode_literals
import re
from django.db import models


class farmers(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=255)
	bio = models.CharField(max_length=255)
	region = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
"""class choice(Field):
	status = models.IntegerField(choices=STATUS_CHOICES, required=True, default=0)
"""	




