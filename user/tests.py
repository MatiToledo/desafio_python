import unittest
from django.test import TestCase
import unittest
import random
import string
from user.forms import AvatarForm, UserEditForm, UserRegisterForm


# Create your tests here.
class UserTestCase(unittest.TestCase):
  def setUp(self):
    pass

  def createUser(self):
    userLen = 20
    keyListUser = [random.choice((string.ascii_letters + string.digits)) for i in range(userLen)] 
    passwordLen = 20
    keyListPassword = [random.choice((string.ascii_letters + string.digits)) for i in range(passwordLen)] 
    
    username = "".join(keyListUser)
    password = "".join(keyListPassword)
    UserRegisterForm(username=username,password=password)
