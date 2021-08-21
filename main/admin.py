from django.contrib import admin
from .models import ToDo
from .models import ToMeet
from .models import Habit


admin.site.register(ToDo)
admin.site.register(ToMeet)
admin.site.register(Habit)

# Register your models here.
