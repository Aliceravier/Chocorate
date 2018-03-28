from django.test import TestCase
from django.contrib.auth.models import User
from chocorate.models import UserProfile, Chocolate


# Create your tests here.


class ModelTests(TestCase):
    # Creating users
    def setUp(self):
        u = User.objects.create(username='test')
        u.set_password('check1234')
        u.save()

    # Test for adding user
    def test_add_user(self):
        u = User.objects.get(username='test')
        p = UserProfile.objects.create(user=u, notifications=1)
        p.save()
        self.assertEqual(u.username == 'test', True)

    # Test for adding chocolate
    def test_add_chocolate(self):
        u = User.objects.get(username='test')
        choco_nums = len(Chocolate.objects.all())
        choco = Chocolate.objects.create(name="test1", description="good choice", picture="",
                                         picture_alt="some image should be here",
                                         picture_url="", chocolate_type="milk", comments="", avgrating=4.5)
        choco.save()
        self.assertEqual(len(Chocolate.objects.all()), choco_nums + 1)

