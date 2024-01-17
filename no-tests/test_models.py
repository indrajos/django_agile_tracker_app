# from django.test import TestCase
# from myapp.models import Story, Task, TimeEntry
# from django.core.exceptions import ValidationError
#
#
# class StoryModelTest(TestCase):
#     def test_calculate_total_task_hours_spent(self):
#         # Create a story
#         story = Story.objects.create(
#             id = 7,
#             title="My Test Story",
#             estimated_hours=5
#         )
#
#         # Create two tasks for the story
#         task1 = Task.objects.create(
#             id = 15,
#             story=story,
#             title="Task 1",
#             estimated_hours=2
#         )
#         task2 = Task.objects.create(
#             id = 16,
#             story=story,
#             title="Task 2",
#             estimated_hours=3
#         )
#
#         # Add some time entries to the tasks
#         time_entry1 = TimeEntry.objects.create(
#             task=task1,
#             hours_spent=1
#         )
#         time_entry2 = TimeEntry.objects.create(
#             task=task2,
#             hours_spent=2
#         )
#
#         # Assert that the total task hours spent is calculated correctly
#         self.assertEqual(story.calculate_total_task_hours_spent(), 3)
#
#
# class TaskModelTest(TestCase):
#     def test_calculate_total_time_spent(self):
#         # Create a story
#         story = Story.objects.create(
#             id=7,
#             title="My Test Story",
#             estimated_hours=5
#         )
#         task = Task.objects.create(
#             id=18,
#             story=story,
#             title="My Test Task",
#             estimated_hours=4
#         )
#
#         # Add some time entries to the task
#
#         time_entry1 = TimeEntry.objects.create(
#             task=task,
#             hours_spent=1
#         )
#         time_entry2 = TimeEntry.objects.create(
#             task=task,
#             hours_spent=2
#         )
#
#         # Assert that the total time spent is calculated correctly
#         self.assertEqual(task.calculate_total_time_spent(), 3)
#
#
# class TimeEntryModelTest(TestCase):
#     def test_is_positive(self):
#         # # Create a time entry with a negative hours spent value
#         time_entry = TimeEntry(task_id=1, hours_spent=-2, description="Worked on the task for 2 hours.")
#
#         # Assert that a ValidationError is raised
#         with self.assertRaises(ValidationError):
#             time_entry.is_positive()
