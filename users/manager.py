from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self,nombre, cedula, email, password=None):
        if not cedula:
            raise ValueError('El usuario debe tener una cedula')
        if not email:
            raise ValueError('El usuario debe tener un email')
        if not nombre:
            raise ValueError('El usuario debe tener un nombre')
        user = self.model(nombre=nombre, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre,cedula, email, password):
        user = self.create_user(nombre, cedula,email, password )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user