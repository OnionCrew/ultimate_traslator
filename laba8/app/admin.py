from django.contrib import admin
from .models import Error, Programmer, ErrorFix

admin.site.register(Error)
admin.site.register(Programmer)
admin.site.register(ErrorFix)
