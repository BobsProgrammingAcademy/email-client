from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import User, Email


class UserModelUnitTestCase(TestCase):
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


class IndexRequestTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='bob@test.com', username='Bob', password='pass123')

    def test_index_view(self):
        client = Client()
        client.login(email=self.user.email, password=self.user.password)
        response = client.get('/')
        self.assertRedirects(response,
                             reverse('login'),
                             status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True)
