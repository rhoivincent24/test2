from django.urls import path
from .views import (HomePageView, AboutPageView, ContentPageView, ResourcesPageView, CommunityPageView,
                    EventsPageView, ContactPageView, LoginPageView,ResourceListView,
    ResourceCreateView,
    ResourceDetailView,
    ResourceUpdateView,
    ResourceDeleteView,)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('resources/', ResourceListView.as_view(), name='resource_list'),
    path('resources/create/', ResourceCreateView.as_view(), name='resource_create'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),  # Fix here
    path('content/', ResourceListView.as_view(), name='content'),
    path('resource/<int:pk>/update/', ResourceUpdateView.as_view(), name='resource_update'),  # Update a resource
    path('resource/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource_delete'),  # Delete a resource
    path('community/', CommunityPageView.as_view(), name='community'),
    path('events/', EventsPageView.as_view(), name='events'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('login/', LoginPageView.as_view(), name='login'),
]
