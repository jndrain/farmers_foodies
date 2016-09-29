from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class farmersManager(models.Manager):
	def register(self, data):
		errors = []
		if not data['email']:
			errors.append ('This is not an email')
		elif EMAIL_REGEX.match['password']:
			errors.append('This is the invalid email')
		if self.filter(email=data['email']):
			errors.append('Account already in use')

		if not data['password']:
			errors.append ('Password cannot be blank.')
		elif len(data["password"]) < 8:
			errors.append("Password must be at least 8 characters long")
		elif data["password"] != data["confirm"]:
			errors.append("Password and confirmation don't match")

		response = {}

		if errors:
			response["registered"] = False
			response["errors"] = errors
		else:
			password = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
			user = self.create(email=data["email"], password=password)

			response["registered"] = True
			response["user"] = user

		return response

	def login(self, data):
		user = self.filter(email=data["email"])

		if not user:
			return False
		else:
			user = user[0]

		if bcrypt.hashpw(data["password"].encode(), user.password.encode()) == user.password.encode():
			return user
		else:
			return False

class farmers(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class farms(models.Model):
	name = models.ForeignKey(max_length=30)
	email = models.ForeignKey(max_length=30)
	address = models.CharField(max_length=30)
	bio = models.CharField(max_length=255)
	region = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = farmersManager()


