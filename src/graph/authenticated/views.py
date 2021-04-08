from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from graphene_django.views import GraphQLView
import rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.settings import api_settings


class DRFAuthenticatedGraphQLView(GraphQLView):
    def parse_body(self, request):
        if isinstance(request, rest_framework.request.Request):
            return request.data
        return super(DRFAuthenticatedGraphQLView, self).parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(DRFAuthenticatedGraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        view = authentication_classes(api_settings.DEFAULT_AUTHENTICATION_CLASSES)(view)
        view = api_view(['GET', 'POST'])(view)
        return view

class AuthView(APIView):
    permission_classes = (IsAuthenticated,)  # <-- And here

    def get(self, request):
        content = {
            "username": f'{request.user}'
        }

        return Response(content)


class UserView(APIView):
    permission_classes = (IsAuthenticated,)  # <-- And here

    def get(self, request):
        user = User.objects.get(username=request.user)
        user = model_to_dict(user)
        user.pop('password')
        user.pop('groups')
        user.pop('user_permissions')

        return Response(user)

    def put(self, request):
        updated_user = request.data

        user = User.objects.get(username=request.user)

        if updated_user['first_name'] is not None:
            user.first_name = updated_user['first_name']

        if updated_user['last_name'] is not None:
            user.last_name = updated_user['last_name']

        if updated_user['email'] is not None:
            user.email = updated_user['email']

        user.save()

        content = model_to_dict(user)

        return Response(content)
