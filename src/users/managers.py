from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, country, gender, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email), username=username, gender=gender, country=country
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, country, gender, password):
        """Create and save a new superuser with given details"""

        user = self.create_user(email, username, country, gender, password)

        user.admin = True
        user.staff = True

        user.save(using=self._db)
        return user
