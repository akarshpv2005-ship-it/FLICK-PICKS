from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Register


class RegisterViewTests(TestCase):
    def test_existing_email_shows_message_instead_of_integrity_error(self):
        user_model = get_user_model()
        user_model.objects.create_user(
            username="existing@example.com",
            password="ExistingPass123",
            usertype="user",
        )

        response = self.client.post(
            "/register/",
            {
                "name": "New User",
                "address": "123 Main Street",
                "phone number": "1234567890",
                "email": "existing@example.com",
                "password": "NewPass123",
            },
        )

        self.assertRedirects(response, "/login/")
        self.assertEqual(user_model.objects.count(), 1)
        self.assertEqual(Register.objects.count(), 0)
