import typing

from django.http import Http404
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
User = get_user_model()

class CheckPasswordBackend(ModelBackend):
    def authenticate(self, request=None, username=None, password=None):
        print("attempting to authenticate with username: {} and password: {}".format(username, password))
        try:
            prelim = User.objects.get(username=username)
            print("seeing that the user exists, with username: {} and password: {}".format(prelim.username, prelim.password))
            print(prelim.check_password(password))
            if prelim.check_password(password):
                return prelim
            else:
                return None

            
        except User.DoesNotExist:
            return None

        return user if user else None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# There once was a boy imprecise
# With two passwords that weren't very nice
# They riddled him with words
# Til he realized the absurd
# My god, I hashed them both twice

#JFC




