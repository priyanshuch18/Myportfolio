from django.shortcuts import render
from .models import Myinfo, About, FrontendSkill, BackendSkill, Projects, Contact

# Create your views here.
def index(request):
    myinfo = Myinfo.objects.all()
    about = About.objects.all()
    frontendskill = FrontendSkill.objects.all()
    backendskill = BackendSkill.objects.all()
    projects = Projects.objects.all()
    contact = Contact.objects.all()
    context = {
        'myinfo': myinfo,
        'about': about,
        'frontendskill': frontendskill,
        'backendskill': backendskill,
        'projects': projects,
        'contact': contact,
        
    }

    return render(request, 'portfolio/index.html', context)
