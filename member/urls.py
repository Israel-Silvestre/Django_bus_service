from rest_framework.routers import DefaultRouter
from member.views import MemberViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'', MemberViewSet, 'member-crud')

urlpatterns = router.urls