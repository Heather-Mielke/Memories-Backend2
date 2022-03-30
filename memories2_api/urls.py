from django.urls import path
from . import views

urlpatterns = [
    path('api/photos', views.PhotoList.as_view(), name='photo_list'), # api/photos will be routed to the PhotoList view for handling
    path('api/photos/<int:pk>', views.PhotoDetail.as_view(), name='photo_detail'), # api/photos will be routed to the PhotoDetail view for handling
]