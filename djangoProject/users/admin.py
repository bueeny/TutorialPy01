from django.contrib import admin
from .models import Profile

# Register your models here.
# Register profile models here and you can see this on webiste/admin django admin page
# But we would want a place to store all these profile pictures within Profile  
admin.site.register(Profile)
