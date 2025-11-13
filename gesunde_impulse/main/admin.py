from django.contrib import admin
from .models import Task, Skill, Attribute


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    display_list = ('name', 'skill', 'completed', 'increment')
    edit_list = ('completed', 'increment')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    display_list = ('name', 'attribute', 'level', 'increment')
    edit_list = ('level', 'increment')


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    display_list = ('name', 'level')
