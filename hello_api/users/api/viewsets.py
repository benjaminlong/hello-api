from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .serializers import UserSerializer


User = get_user_model()


class UserViewSet(RetrieveModelMixin,
                  ListModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    serializer_class = UserSerializer
    lookup_field = "username"
    queryset = User.objects.select_related('primary_role').prefetch_related('roles')

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
