from users.models import User
from django.contrib.auth.backends import ModelBackend

class ModelBackendExtended(ModelBackend):
  def authenticate(self, username=None, password=None):
  #def authenticate(self, username=None, email=None, password=None):
    try:
      user = User.objects.get(cedula=username)
      if user.check_password(password):
        return user
    except User.DoesNotExist:
    #except (User.DoesNotExist, IndexError):
      return None