from .models import CustomUser
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from .models import LoftRentals, TemporaryStandRental, CoMinimizing, MaintenanceAndHousekeeping, ConnectedAppliance, LoftFeature

# Register your models
admin.site.register(LoftRentals)
admin.site.register(TemporaryStandRental)
admin.site.register(CoMinimizing)
admin.site.register(MaintenanceAndHousekeeping)
admin.site.register(ConnectedAppliance)
admin.site.register(LoftFeature)

# Update the LogEntry user field to use the correct import path
LogEntry._meta.get_field('user').remote_field.model = get_user_model()

# Remove the LogEntryAdmin class if it exists
if admin.site._registry.get(LogEntry):
    admin.site.unregister(LogEntry)

# Define a new LogEntryAdmin class
class CustomLogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message']
    list_filter = ['content_type']
    search_fields = ['user__username', 'object_repr', 'change_message']

# Register the new LogEntryAdmin class
admin.site.register(LogEntry, CustomLogEntryAdmin)
