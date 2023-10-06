from django.contrib import admin
from .models import Milestone, Tag

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'parent', 'description',)
    list_filter = ('user',)
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)