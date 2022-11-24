from django.contrib import admin

# Register your models here.
from .models import Project,teamDetails,postLikes

admin.site.register(Project)
admin.site.register(teamDetails)
admin.site.register(postLikes)


