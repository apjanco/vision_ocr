from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class vision(models.Model):
	RUSSIAN = 'Ru'
	AZERBAIJANI = 'az'
	BELARUSIAN = 'be'
	BULGARIAN = 'bg'
	CROATIAN = 'hr'	
	CZECH = 'cs'
	ESTONIAN = 'et'	
	HUNGARIAN = 'hu'
	KAZAKH = 'kk'
	KYRGYZ = 'ky'
	LATVIAN = 'lv'
	LITHUANIAN = 'lt'
	MACEDONIAN = 'mk'		
	POLISH = 'pl'
	ROMANIAN = 'ro'
	SERBIAN = 'sr'
	SLOVAK = 'sk'
	SLOVENIAN = 'sl'		
	SPANISH = 'Es'
	UKRAINIAN = 'uk'
	UZBEK = 'uz'
	NONE = '-'
	LANGUAGE_CHOICES = ((NONE, '-'),(RUSSIAN, 'Russian'), (AZERBAIJANI, 'Azerbaijani'), (BELARUSIAN, 'Belarusian'),(BULGARIAN, 'Bulgarian'),(CROATIAN,'Croatian'),(CZECH, 'Czech'),(ESTONIAN, 'Estonian'),(HUNGARIAN,'Hungarian'),(KAZAKH,'Kazakh'),(KYRGYZ,'Kyrgyz'),(LATVIAN, 'Latvian'),(LITHUANIAN,'Lithuanian'),(MACEDONIAN, 'Macedonian'),(POLISH, 'Polish'),(ROMANIAN, 'Romanian'),(SERBIAN, 'Serbian'),(SLOVAK, 'Slovak'),(SLOVENIAN, 'Slovenian'),(SPANISH, 'Spanish'),(UKRAINIAN, 'Ukrainian'),(UZBEK, 'Uzbek'))

	language = models.CharField(max_length = 5, choices=LANGUAGE_CHOICES, default=NONE)
	
	created_at = models.DateTimeField(auto_now_add=True)

	file = models.FileField(blank=True, storage=FileSystemStorage(location='/Users/ajanco/tmp/'))
	
	text = models.TextField(default='', blank=True)

	
