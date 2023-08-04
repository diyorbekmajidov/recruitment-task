from django.contrib import admin

# qanday qilib models folder dan models.py faylidan User, Investor, Project klasslarini import qilish kerak?
from api.models import User, Investor, Project

admin.site.register(User)
admin.site.register(Investor)
admin.site.register(Project)
