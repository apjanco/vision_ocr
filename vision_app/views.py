from django.shortcuts import render
from django.views.generic.edit import FormView
from vision_app.forms import FileFieldForm

import tempfile
from google.cloud import vision
import base64
import googleapiclient.discovery
import io
import pprint
import os 

API_KEY = 'AIzaSyBZZcmX_W0rFAJUmHbLnQyOGOxJqdm902w'


def google_vision(photo_file, language):
	if language == '-':
		language = ''
	else:
		pass

	service = googleapiclient.discovery.build('vision', 'v1', developerKey=API_KEY)

	service_request = service.images().annotate(body={
               'requests': [{
                   'image': {
                       'content': photo_file.decode('UTF-8')
                        },
                    'imageContext': {
                        'languageHints': [language]},
                    'features': [{
                        'type': 'TEXT_DETECTION'
                    }]
                }]
            })
	response = service_request.execute()
	label = response['responses'][0]['textAnnotations'][0]['description']
	label = label.encode('utf-8')
	return label
        
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = FileFieldForm(request.POST, request.FILES)
		if form.is_valid():
			language = str(form['language'].value)
			photo_file = base64.b64encode(request.FILES['file'].read())
			text = google_vision(photo_file, language)

		



			return render(request, 'index.html',{'form':form,'text':text})

		else:
			print(form.errors)
	else:
		form = FileFieldForm()

		return render(request, 'index.html',{'form':form})
    
 