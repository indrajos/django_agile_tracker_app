from django.db import models
from django.core.exceptions import ValidationError


class Story(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, null=False)
    title = models.CharField(max_length=255)
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    total_hours_spent = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def calculate_total_task_hours_spent(self):
        # Get all tasks related to this story
        tasks = Task.objects.filter(story=self)

        total_task_hours_spent = 0

        # Iterate through the tasks and sum the task_hours_spent
        for task in tasks:
            total_task_hours_spent += task.task_hours_spent

            # Add time spent on all time entries related to this task
            time_entries = TimeEntry.objects.filter(task=task)
            total_task_hours_spent += sum(time_entry.hours_spent for time_entry in time_entries)

        return total_task_hours_spent

    # def __str__(self):
    #     return self.title


class Task(models.Model):
    status_choices = (
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    id = models.BigAutoField(primary_key=True, auto_created=True, null=False)
    title = models.CharField(max_length=255)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=False, blank=False)
    status = models.CharField(max_length=20, choices=status_choices, default='To Do')
    task_hours_spent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def calculate_total_time_spent(self):
        time_entries = TimeEntry.objects.filter(task=self)
        total_time_spent = sum(entry.hours_spent for entry in time_entries)
        return total_time_spent


class TimeEntry(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, blank=False)
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    description = models.TextField()
    developer = models.CharField(max_length=255, null=False)

    def is_positive(self):
        if self.hours_spent < 0:
            raise ValidationError("The hours spent cannot be negative.")

        # super().clean()

    def __str__(self):
        return f"Time Entry for {self.task.title}"


class Developer(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, null=False)
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name