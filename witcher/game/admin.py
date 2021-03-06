from django.contrib import admin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'external_id',
        'name',
        'experience',
        'karma',
        'total',
        'position'
    )


admin.site.register(Profile, ProfileAdmin)
