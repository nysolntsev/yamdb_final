from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .permissions import IsAdmin
from .serializers import AdminSerializer, TokenSerializer, UserSerializer


def confirmation_code_and_send_email(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='Confirmation code',
        message=f'Ваш код подтверждения: {confirmation_code}',
        from_email=None,
        recipient_list=[user.email]
    )


class SignUpView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.data['email']
            username = serializer.data['username']
            confirmation_code_and_send_email(username)
            return Response({
                'email': email,
                'username': username},
                status=status.HTTP_200_OK)
        if 'username' or 'email' not in serializer.data:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(email=email)
        if not user:
            new_user = User(username=username, email=email)
            new_user.save()
            return Response(
                {'email': new_user.email,
                 'username': new_user.username},
                status=status.HTTP_200_OK)
        return Response(status=status.HTTP_409_CONFLICT)


class UsersView(APIView):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user.username)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def patch(self, request):
        user = get_object_or_404(User, username=request.user.username)
        serializer = UserSerializer(
            user,
            data=request.data,
            partial=True,
            many=False
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (IsAdmin,)
    lookup_field = 'username'


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(
                User,
                username=serializer.data['username']
            )
            if (default_token_generator.check_token(
                    user, serializer.data['confirmation code'])):
                token = AccessToken.for_user(user)
                return Response(
                    {'token': token}, status=status.HTTP_200_OK
                )
            return Response(
                {'confirmation code': 'Неправильный код'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if 'username' or 'confirmation code' not in serializer.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
