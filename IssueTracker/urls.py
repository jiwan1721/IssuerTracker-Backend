from django.urls import path,include

from IssueTracker.serializers import UserIssueSerializers
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import IssueView,UserView,UserIssueView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user',views.UserView,basename='user')
router.register(r'assigned-issues',views.IssueView,basename='issues')
router.register(r'admin-user',views.AdminViewSet,basename='for-admin-only')
router.register(r'user-specific-issue',views.UserZero,basename='userIssue')

app_name = 'Issue'

urlpatterns = [
    path('',include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
