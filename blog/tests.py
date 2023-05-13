from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserCommentForm, UserAddPostForm, UserPostEditForm


class TestUserCommentForm(TestCase):
    def test_post_user_content_input_is_required(self):
        """
        Tests if the required restriction for comment form behaves as expected.
        """
        form = UserCommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')


class TestUserAddPostForm(TestCase):
    def test_post_user_content_input_is_required(self):
        """
        Tests if the required restriction for add post form behaves as expected.
        """
        form = UserCommentForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

