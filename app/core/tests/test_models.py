from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'varannik@gmail.com'
        password = 'test'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        "test the email for a new user is normalized"
        email = 'varanik@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test')

        self.assertEqual(user.email,email.lower())
    
    def test_new_user_invalid(self):
        """ test creating user with  no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_ne_superuser(self):
        user = get_user_model().objects.create_superuser(
            'varanik5@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
