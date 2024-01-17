# from django.test import TestCase
# from django.urls import reverse
# from myapp.models import Story, Task, TimeEntry
# from myapp.forms import StoryForm, TaskForm, TimeEntryForm
#
#
# class MyappViewsTestCase(TestCase):
#     def test_create_story_view(self):
#         response = self.client.get(reverse('create_story'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'story_form.html')
#
#         form_data = {
#             'title': 'Test Story',
#             'estimated_hours': 10.0,
#         }
#         response = self.client.post(reverse('create_story'), form_data)
#         self.assertEqual(response.status_code, 302)  # Check for a redirect upon successful form submission
#         self.assertRedirects(response, reverse('story_list'))
#
#         # Add more test cases based on your requirements
#
#     def test_create_task_view(self):
#         story = Story.objects.create(title='Test Story', estimated_hours=10.0)
#         response = self.client.get(reverse('create_task', args=[story.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'create_task.html')
#
#         form_data = {
#             'title': 'Test Task',
#             'status': 'To Do',
#             'estimated_hours': 5.0,
#         }
#         response = self.client.post(reverse('create_task', args=[story.id]), form_data)
#         self.assertEqual(response.status_code, 302)  # Check for a redirect upon successful form submission
#         self.assertRedirects(response, reverse('task_list', args=[story.id]))
#
#         # Add more test cases based on your requirements
#
#     def test_create_time_entry_view(self):
#         story = Story.objects.create(id=8, title='Test Story', estimated_hours=10)
#         task = Task.objects.create(
#             id=10,
#             title='Test Task',
#             status='To Do',
#             estimated_hours=5,
#             story=story,
#
#         )
#         response = self.client.get(reverse('create_time_entry', args=[task.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'create_time_entry.html')
#
#         form_data = {
#             'hours_spent': 2.5,
#             'description': 'Test description',
#             'developer': 'Indrajos',
#             'status': 'In Progress',
#         }
#         response = self.client.post(reverse('create_time_entry', args=[task.id]), form_data)
#         #print(response)
#         self.assertEqual(response.status_code, 200)
#
