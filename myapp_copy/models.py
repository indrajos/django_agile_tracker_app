from django.db import models


class Story(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2)
    total_hours_spent = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def calculate_total_task_hours_spent(self):
        tasks = self.task_set.all()
        total_task_hours_spent = sum(task.task_hours_spent for task in tasks)
        return total_task_hours_spent

    def __str__(self):
        return self.title


class Task(models.Model):
    status_choices = (
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    title = models.CharField(max_length=255)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)  # a foreign key relationship with the Story model
    status = models.CharField(max_length=20, choices=status_choices, default='To Do')
    task_hours_spent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2)

    def calculate_total_time_spent(self):
        time_entries = TimeEntry.objects.filter(task=self)
        total_time_spent = sum(entry.hours_spent for entry in time_entries)
        return total_time_spent


class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)  # Establish a foreign key relationship with the Task model
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    developer = models.CharField(max_length=255)

    def __str__(self):
        return f"Time Entry for {self.task.title}"


class Developer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
