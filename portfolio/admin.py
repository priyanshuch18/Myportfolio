from django.contrib import admin
from .models import Myinfo, About, FrontendSkill, BackendSkill, Projects, Contact

# Register your models here.
admin.site.register(Myinfo)
admin.site.register(About)
admin.site.register(FrontendSkill)
admin.site.register(BackendSkill)
admin.site.register(Projects)
admin.site.register(Contact)
