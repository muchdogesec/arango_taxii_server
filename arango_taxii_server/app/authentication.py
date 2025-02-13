from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .arango_helper import ArangoSession


class ArangoUser(AnonymousUser):
    app_label = "arango_taxii_server"

    def __init__(self, username, passwd):
        self.username = username
        self.arango_auth = (username, passwd)
        self.arango_session = ArangoSession(*self.arango_auth)

    @property
    def is_authenticated(self):
        # Always return True. This is a way to tell if
        # the user has been authenticated in permissions
        return True

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    def __str__(self):
        return f"ArangoUser({self.username})"


class ArangoServerAuthentication(BasicAuthentication):
    def authenticate_credentials(self, userid, password, request=None):
        """
        Authenticate the userid and password against username and password
        with optional request for context.
        """
        user = ArangoUser(userid, password)

        if user is None:
            raise AuthenticationFailed("Invalid username/password.")

        return (user, None)
