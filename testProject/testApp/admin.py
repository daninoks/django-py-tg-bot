from django.contrib import admin

from .models import Profile
from .models import Message
from .forms import ProfileForm

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')

    # def get_queryset(self, request):
    #     return
