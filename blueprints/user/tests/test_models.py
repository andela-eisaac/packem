from django.test import TestCase

from blueprints.user import models


class UserTestCase(TestCase):
    def setUp(self):
        self.user = models.User.objects.create(email='foo@bar.com', first_name='foo',
                                               last_name='bar', password='fooBar')

    def test_user_creation(self):
        self.assertTrue(self.user, models.User)

    def test_password_is_encrypted(self):
        self.assertNotEqual(self.user.password, 'fooBar')