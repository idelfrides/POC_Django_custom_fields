from django.contrib import admin
from .models import Developer


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role', 'company', 'gender', 'age', 'update', 'id']
    list_editable = ['full_name']
    list_filter = ['role', 'company']
    list_display_links  = ['update']
    search_fields = ['gender']

    class Meta:
        model = Developer


admin.site.register(Developer, DeveloperAdmin)