
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from hello_api.items.models import Item
from hello_api.items.api.serializers import ItemSerializer


class AuthenticatedItemViewSet(ListModelMixin, GenericViewSet):
    permission_classes = ()
    pagination_class = PageNumberPagination
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super(AuthenticatedItemViewSet, self).get_queryset()
        queryset.filter(owner=self.request.user)
