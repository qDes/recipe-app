from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="test@example.com", password="testpass"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = "test@example.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
                email=email,
                password=password
                )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_news_user_email_normalized(self):
        """Test the email for new user is normalized."""
        email = "test@EXAMPLE.COM"
        user = get_user_model().objects.create_user(email, 'test234352')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test234234')

    def test_create_new_super_user(self):
        """Test creating a news superuser"""
        user = get_user_model().objects.create_superuser(
                'test@example.com',
                'test523532'
                )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
                user=sample_user(),
                name="Vegan"
        )

        self.assertEqual(str(tag), tag.name)
