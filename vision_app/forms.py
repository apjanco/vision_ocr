#forms.py
from django import forms
from django.db import models
from django.core.files.storage import FileSystemStorage
from vision_app.models import vision



class FileFieldForm(forms.ModelForm):
	class Meta:
		model = vision
		fields = ('file','language')
		#file = models.FileField(label='')
