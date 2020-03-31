from django.contrib import admin
from .models import Contact,Updates,Sypmtoms
# Register your models here.

class AdminContact(admin.ModelAdmin):
    search_fields = ["pk","name","message"]
    list_filter = ["name","created_at"]
    list_display = [
        "pk",
        "name",
        "email",
        "created_at",
        "message"
    ]

class AdminUpdates(admin.ModelAdmin):
  list_display = [
    "pk",
    "active",
    "recover",
    "death",
  ]

class AdminSymptoms(admin.ModelAdmin):
  list_display = [
    "pk",
    "sym",
  ]  
admin.site.register(Updates,AdminUpdates)
admin.site.register(Sypmtoms,AdminSymptoms)
admin.site.register(Contact,AdminContact)