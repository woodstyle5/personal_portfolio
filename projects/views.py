from django.shortcuts import render

# Create your views here.
def project_index(request):
	projects = Project.object.all()
	context = {
		'projects' : projects
	}
	return render(request, 'project_index.html',context)