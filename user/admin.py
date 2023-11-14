from django.contrib import admin
from .models import Student, College, Branch,Material
# Register your models here.

admin.site.register(Student)
admin.site.register(College)
admin.site.register(Branch)
admin.site.register(Material)