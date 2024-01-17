# from django.test import TestCase
# from myapp.forms import TimeEntryForm
# from myapp.models import TimeEntry, Developer, Task, Story
#
#
# class TimeEntryFormTest(TestCase):
#     def setUp(self):
#         # Create a sample developer for the form
#         self.developer = Developer.objects.create(name='Test Developer')
#
#         # Create a sample story and task for the form
#         self.story = Story.objects.create(title='Test Story', estimated_hours=20)
#         self.task = Task.objects.create(title='Test Task', estimated_hours=10)
#
#     def test_time_entry_form_valid(self):
#         form_data = {
#             'hours_spent': 5.0,
#             'description': 'Test description',
#             'developer': self.developer.id,  # Use the ID of the sample developer
#             'status': 'In Progress',
#         }
#         form = TimeEntryForm(data=form_data)
#
#         self.assertTrue(form.is_valid())
#
#     def test_time_entry_form_save(self):
#         form_data = {
#             'hours_spent': 5.0,
#             'description': 'Test description',
#             'developer': self.developer.id,  # Use the ID of the sample developer
#             'status': 'In Progress',
#         }
#         form = TimeEntryForm(data=form_data)
#
#         self.assertTrue(form.is_valid())
#
#         # Save the form
#         time_entry = form.save()
#         self.assertIsNotNone(time_entry)
#
#         # Check if the time entry task status was updated
#         if self.task:
#             self.task.refresh_from_db()
#             self.assertEqual(self.task.status, 'In Progress')
