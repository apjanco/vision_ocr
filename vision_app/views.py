from django.shortcuts import render
from django.views.generic.edit import FormView
from vision_app.forms import FileFieldForm
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = FileFieldForm(request.POST, request.FILES)
		if form.is_valid():
			return render(request, 'index.html',{'form':form})

		else:
			print(form.errors)
	else:
		form = FileFieldForm()

		return render(request, 'index.html',{'form':form})
    
 