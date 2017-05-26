from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.staff_base_info)
admin.site.register(models.staff_action_log)
admin.site.register(models.ordered_list)

