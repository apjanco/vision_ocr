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
from wand.image import Image
import shutil



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
			print(language + "this is the language")
			file_name = str(request.FILES['file'].name)

			file_extension = str(file_name).lower().split('.')[1]
			print (file_extension)
			if file_extension == 'jpg' or file_extension == 'jpeg':
				print("nice it's a jpeg")

				photo_file = base64.b64encode(request.FILES['file'].read())
				texts = []
				text = google_vision(photo_file, language)
				texts.append(text)

			if file_extension == 'pdf':
				print("it's a little pdf!")
				pdf_file = request.FILES['file'].read()
				with tempfile.NamedTemporaryFile(suffix='.txt', dir='/tmp', delete=False) as f:
					f.write(pdf_file)
					f.close()

					with Image(filename=f.name, resolution=200) as img:
						img.format = 'jpeg'
						if not os.path.exists('/tmp/jpg/'):
							os.makedirs('/tmp/jpg/')
						img.save(filename='/tmp/jpg/v_ocr.jpg')

						texts = []
						for jpg_file in os.listdir('/tmp/jpg/'):
							with open('/tmp/jpg/' + jpg_file, 'rb') as image:
								image = base64.b64encode(image.read())
								print(jpg_file)
								text = google_vision(image, language)
								texts.append(text)
						
						shutil.rmtree('/tmp/jpg/')
						print("deleted temp directory")
			else:
				form = FileFieldForm()




			return render(request, 'index.html',{'form':form,'texts':texts,'file_name':file_name})

		else:
			print(form.errors)
	else:
		form = FileFieldForm()

		return render(request, 'index.html',{'form':form})
    
 
