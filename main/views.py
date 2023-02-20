from django.shortcuts import render, get_object_or_404
from .models import Project, Contact, Info
from .forms import ContactForm

# Create your views here.


def index(request):
	info = Info.objects.all()
	projects = Project.objects.all()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your message has been sent sucessfully!')
			return redirect('index')
	else:
		form = ContactForm()
	return render(request,'portfolio/index.html', {'info':info, 'projects':projects, 'form': form })


def projectDetails(request,pk):
	projects = get_object_or_404(Project, pk=pk)
	return render(request,'portfolio/project-details.html', {'projects':projects})

