from rest_framework.routers import DefaultRouter
from seap.views import EventViewSet, CommentViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'comments', CommentViewSet)