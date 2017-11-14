from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class vision(models.Model):
	RUSSIAN = 'Ru'
	SPANISH = 'Es'
	NONE = ''
	LANGUAGE_CHOICES = ((NONE, ''),(RUSSIAN, 'Ru'), (SPANISH, 'Es'))

	language = models.CharField(max_length = 5, choices=LANGUAGE_CHOICES, default=NONE)
	
	created_at = models.DateTimeField(auto_now_add=True)

	file = models.FileField(blank=True, storage=FileSystemStorage(location='/tmp/'))
	
	text = models.TextField(default='', blank=True)

	