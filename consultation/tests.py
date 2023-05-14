from django.test import TestCase
from django.contrib.auth.models import User
from .forms import ApplicationForm


class TestViews(TestCase):
    def setUp(self):
        """
        Generate a test account to test if users can access areas
        that require logins.
        """
        testuser = User.objects.create_user(
            username="test_account",
            password="test_pass",
            email="test@email.com"
        )
        testuser.save()

    def test_consultation_apply_view(self):
        self.client.login(username="test_account", password="test_pass")
        response = self.client.get('/consultation/apply/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'consultation/consultation-list.html')

    def test_consultation_apply_view_logout(self):
        """
        Tests if users can enter the application page when not logged in.
        """
        self.client.login(username="test_account", password="test_pass")
        self.client.logout()
        response = self.client.get('/consultation/apply/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'consultation/consultation-list.html')

    def test_consultation_add_application_view(self):
        """
        Tests if logged in users can access the application form.
        """
        self.client.login(username="test_account", password="test_pass")
        response = self.client.get('/consultation/application-form/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultation/add_application.html')


class TestApplicationForm(TestCase):
    def test_content_is_required(self):
        """
        Tests if the required restriction
        for add application form behaves as expected.
        """
        form = ApplicationForm({'phone': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors.keys())
        self.assertEqual(form.errors['phone'][0], 'This field is required.')
