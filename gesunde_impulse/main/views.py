from django.shortcuts import render, redirect
from .models import Task, Skill, Attribute


# Create your views here.

def task_list(request):
    tasks = Task.objects.all()   # fetch all tasks from the database
    return render(request, 'task_list.html', {'tasks': tasks})


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if not task.completed:
        task.completed = True
        task.save()

        # Increase Skill by Task increment
        skill = task.skill
        skill.level += task.increment
        skill.save()

        # Increase Attribute by Skill increment
        attribute = skill.attribute
        attribute.level += skill.increment
        attribute.save()

    return redirect('task_list')


def home(request):
    skills = Skill.objects.all()
    attributes = Attribute.objects.all()
    return render(request, 'home.html', {
        'skills': skills,
        'attributes': attributes
    })
