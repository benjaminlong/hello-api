from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from hello_api.users.api import viewsets as users_viewsets

if settings.DEBUG:
    router = DefaultRouter(trailing_slash=settings.APPEND_SLASH)
else:
    router = SimpleRouter(trailing_slash=settings.APPEND_SLASH)


app_name = "api"

# Register your APIs viewsets bellow
# {hostname}/
router.register("users", users_viewsets.UserViewSet)
# router.register("item_comments", items_viewsets.ItemViewSet, basename='item-comments')



urlpatterns = router.urls
