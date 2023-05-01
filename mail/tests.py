from django.test import TestCase
from django.utils import timezone
from .models import User, Email


class ModelTesting(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='john@test.com', username='John', password='pass123')

    def test_user_model(self):
        data = self.user
        self.assertTrue(isinstance(data, User))
        self.assertIsInstance(data, User)
        self.assertEqual(str(data.username), 'John')


class EmailModelUnitTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='bob@test.com', username='Bob', password='pass123')
        self.user2 = User.objects.create(email='john@test.com', username='John', password='pass123')
        self.email = Email.objects.create(
            user=self.user1,
            sender=self.user1,
            subject='New email',
            body='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            timestamp=timezone.now(),
            read=False,
            archived=False
        )
        self.email.recipients.add(self.user2)

    def test_email_model(self):
        data = self.email
        self.assertTrue(isinstance(data, Email))
        self.assertIsInstance(data, Email)
