from django.test import TestCase
from .models import Story, Task, TimeEntry, Developer
from django.core.exceptions import ValidationError
from .forms import StoryForm, TaskForm, TimeEntryForm
from django.urls import reverse


class StoryModelTest(TestCase):
    def test_calculate_total_task_hours_spent(self):
        # Create a story
        story = Story.objects.create(
            id=7,
            title="My Test Story",
            estimated_hours=5
        )

        # Create two tasks for the story
        task1 = Task.objects.create(
            id=15,
            story=story,
            title="Task 1",
            estimated_hours=2
        )
        task2 = Task.objects.create(
            id=16,
            story_id=story.id,
            title="Task 2",
            estimated_hours=3
        )

        # Add some time entries to the tasks
        time_entry1 = TimeEntry.objects.create(
            task=task1,
            hours_spent=1
        )
        time_entry2 = TimeEntry.objects.create(
            task=task2,
            hours_spent=2
        )

        # Assert that the total task hours spent is calculated correctly
        self.assertEqual(story.calculate_total_task_hours_spent(), 3)


class TaskModelTest(TestCase):
    def test_calculate_total_time_spent(self):
        # Create a story
        story = Story.objects.create(
            id=7,
            title="My Test Story",
            estimated_hours=5
        )
        task = Task.objects.create(
            id=18,
            story=story,
            title="My Test Task",
            estimated_hours=4
        )

        # Add some time entries to the task

        time_entry1 = TimeEntry.objects.create(
            task=task,
            hours_spent=1
        )
        time_entry2 = TimeEntry.objects.create(
            task=task,
            hours_spent=2
        )

        # Assert that the total time spent is calculated correctly
        self.assertEqual(task.calculate_total_time_spent(), 3)


class TimeEntryModelTest(TestCase):
    def test_is_positive(self):
        # # Create a time entry with a negative hours spent value
        time_entry = TimeEntry(task_id=1, hours_spent=-2, description="Worked on the task for 2 hours.")

        # Assert that a ValidationError is raised
        with self.assertRaises(ValidationError):
            time_entry.is_positive()


class TimeEntryFormTest(TestCase):
    def setUp(self):
        # Create a sample developer for the form
        self.developer = Developer.objects.create(name='Test Developer')

        # Create a sample story and task for the form
        self.story = Story.objects.create(title='Test Story', estimated_hours=20)
        self.task = Task.objects.create(story_id=self.story.id, title='Test Task', estimated_hours=10)

    def test_time_entry_form_valid(self):
        form_data = {
            'task_id': self.task.id,
            'hours_spent': 5.0,
            'description': 'Test description',
            'developer': self.developer.id,  # Use the ID of the sample developer
            'status': 'In Progress',
        }
        form = TimeEntryForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_time_entry_form_save(self):
        form_data = {
            'task_id': self.task.id,
            'hours_spent': 5.0,
            'description': 'Test description',
            'developer': self.developer.id,  # Use the ID of the sample developer
            'status': 'In Progress',
        }
        form = TimeEntryForm(data=form_data)

        self.assertTrue(form.is_valid())


class MyappViewsTestCase(TestCase):
    def test_create_story_view(self):
        response = self.client.get(reverse('create_story'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'story_form.html')

        form_data = {
            'title': 'Test Story',
            'estimated_hours': 10.0,
        }
        response = self.client.post(reverse('create_story'), form_data)
        self.assertEqual(response.status_code, 302)  # Check for a redirect upon successful form submission
        self.assertRedirects(response, reverse('story_list'))


    def test_create_task_view(self):
        story = Story.objects.create(title='Test Story', estimated_hours=10.0)
        response = self.client.get(reverse('create_task', args=[story.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_task.html')

        form_data = {
            'title': 'Test Task',
            'status': 'To Do',
            'estimated_hours': 5.0,
        }
        response = self.client.post(reverse('create_task', args=[story.id]), form_data)
        self.assertEqual(response.status_code, 302)  # Check for a redirect upon successful form submission
        self.assertRedirects(response, reverse('task_list', args=[story.id]))


    def test_create_time_entry_view(self):
        story = Story.objects.create(id=8, title='Test Story', estimated_hours=10)
        task = Task.objects.create(
            id=10,
            title='Test Task',
            status='To Do',
            estimated_hours=5,
            story=story,

        )
        response = self.client.get(reverse('create_time_entry', args=[task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_time_entry.html')

        form_data = {
            'hours_spent': 2.5,
            'description': 'Test description',
            'developer': 'Indrajos',
            'status': 'In Progress',
        }
        response = self.client.post(reverse('create_time_entry', args=[task.id]), form_data)
        self.assertEqual(response.status_code, 200)
