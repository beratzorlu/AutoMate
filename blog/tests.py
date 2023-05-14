from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserCommentForm, UserAddPostForm, UserPostEditForm

# BLOG APP VIEWS TESTS


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

    def test_blog_list(self):
        """
        Test if test account can access blog list view when logged in.
        """
        self.client.login(username="test_account", password="test_pass")
        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_list.html')

    def test_blog_list_logout(self):
        """
        Test if logging out does not restrict access to blog list view.
        """
        self.client.login(username="test_account", password="test_pass")
        self.client.logout()
        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_list.html')

    def test_add_post(self):
        """
        Test if logged in test account can access add post view.
        """
        self.client.login(username="test_account", password="test_pass")
        response = self.client.get('/add-post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

# BLOG APP FORM TESTS


class TestUserCommentForm(TestCase):
    def test_user_comment_input_is_required(self):
        """
        Tests if the required restriction
        for comment form behaves as expected.
        """
        form = UserCommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')


class TestUserAddPostForm(TestCase):
    def test_add_post_input_is_required(self):
        """
        Tests if the required restriction
        for add post form behaves as expected.
        """
        form = UserAddPostForm({'title': ''}, )
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
