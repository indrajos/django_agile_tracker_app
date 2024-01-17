from django.contrib import admin
from .models import Story, Task, TimeEntry, Developer


admin.site.register(Story)
admin.site.register(Task)
admin.site.register(TimeEntry)
admin.site.register(Developer)