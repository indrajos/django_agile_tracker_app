from django.shortcuts import render, get_object_or_404, redirect
from .models import Story, Task, TimeEntry
from .forms import StoryForm, TaskForm, TimeEntryForm


def home(request):
    stories = Story.objects.all()
    return render(request, 'home.html', {'stories': stories})


def story_list(request):
    stories = Story.objects.all()
    return render(request, 'story_list.html', {'stories': stories})


def task_list(request, id):
    story = get_object_or_404(Story, id=id)
    tasks = Task.objects.filter(story=story)

    context = {
        'story': story,
        'tasks': tasks,
    }

    return render(request, 'task_list.html', context)


def time_entry_list(request, id):
    task = get_object_or_404(Task, id=id)
    time_entries = TimeEntry.objects.filter(task=task)

    return render(request, 'time_entry_list.html', {'task': task, 'time_entries': time_entries})


def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('story_list')
    else:
        form = StoryForm()
    return render(request, 'story_form.html', {'form': form})


def create_task(request, id):
    story = Story.objects.get(id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.story = story
            task.save()
            return redirect('task_list', id=id)

    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'story': story, 'form': form})


def create_time_entry(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        form = TimeEntryForm(request.POST, initial={'developer': request.user})
        if form.is_valid():
            time_entry = form.save(commit=False)
            time_entry.task = task
            time_entry.save()  # Save the time entry

            # Update the task's time spent
            task.task_hours_spent += time_entry.hours_spent
            task.save()

            # Update the task status based on your criteria
            if task.task_hours_spent >= task.estimated_hours:
                task.status = 'Completed'
            else:
                task.status = 'In Progress'
            task.save()

            # Update the associated story's total hours spent
            if task.story:
                task.story.total_hours_spent += time_entry.hours_spent
                task.story.save()

            return redirect('task_list', id=task.story.id)  # Redirect to the task list view upon successful submission

    else:
        form = TimeEntryForm()

    return render(request, 'create_time_entry.html', {'task': task, 'form': form})
