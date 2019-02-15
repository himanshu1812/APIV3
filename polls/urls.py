from django.urls import path
from .views import ( 
    UserCreateAPIView,
    RoomCreateAPIView,
    UserLoginApiView,
)

urlpatterns = [
    path('api/register/',UserCreateAPIView.as_view(),name='apiregister'),
    path('api/room/',RoomCreateAPIView.as_view(),name='addroom'),
    path('api/login/',UserLoginApiView.as_view())
]