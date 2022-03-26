from django.test import TestCase
from todos.models import Todo
from django.contrib.auth.models import User



class ViewsTestCase(TestCase):

    def setUp(self):
        user_record = User.objects.create(username="user", password="user")
        todo = Todo.objects.create(
            title="workout",
            description="go to gym at morning 9am",
            completed=True,
            user=user_record
            )

    def test_todotitle(self):
        todo_title = Todo.objects.get(title="workout")
        
        self.assertEqual(todo_title.description, "go to gym at morning 9am")

    def test_tododescription(self):
        todo_description = Todo.objects.get(description="go to gym at morning 9am")
        self.assertEqual(todo_description.title, "workout")
