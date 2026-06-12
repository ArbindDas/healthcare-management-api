
from django.urls import path
from .views import TestDetailView, TestListCreateView

urlpatterns = [
    
    path('tests/', TestListCreateView.as_view(), name="test-list-create"),
    path('tests/<int:pk>/', TestDetailView.as_view(), name="test-detail-view")
    
]
