from django.urls import path
from .views import IndexView, AboutMeView, AdminInterfaceView  # ADD AdminInterfaceView here

app_name = 'jcJourney'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutMeView.as_view(), name='about_me'),
    path('admin-interface/', AdminInterfaceView.as_view(), name='admin_interface'),  # ADD THIS LINE
]