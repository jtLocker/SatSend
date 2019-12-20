from django.contrib import admin
from .models import Profile
# Register your models here.


#register profile to monitor on admin page
admin.site.register(Profile)