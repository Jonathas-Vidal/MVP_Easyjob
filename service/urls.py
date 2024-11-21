from django.urls import path
from .views import (
    ServiceListView,
    MyServiceListView,
    ServiceSearchView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView
)

urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('my-services/', MyServiceListView.as_view(), name='my-services'),
    path('search/', ServiceSearchView.as_view(), name='service-search'),
    path('<uuid:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('create/', ServiceCreateView.as_view(), name='service-create'),
    path('<uuid:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('<uuid:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
]
