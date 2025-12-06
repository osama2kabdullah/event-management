from django.urls import path
from events.views import dashboard, event_list, event_detail, event_create, event_update, event_delete, category_list, category_create, category_update, category_delete, participant_list, participant_create, participant_update, participant_delete, search_events, home, event_add_participants

urlpatterns = [
    # home
    path('', home, name='home'),

    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),

    # Events
    path('events/', event_list, name='event_list'),
    path('events/add/', event_create, name='event_create'),
    path('events/<int:id>/', event_detail, name='event_detail'),
    path('events/<int:id>/edit/', event_update, name='event_update'),
    path('events/<int:id>/delete/', event_delete, name='event_delete'),
    path('events/<int:id>/add-participants/', event_add_participants, name='event_add_participants'),

    # Categories
    path('categories/', category_list, name='category_list'),
    path('categories/add/', category_create, name='category_create'),
    path('categories/<int:id>/edit/', category_update, name='category_update'),
    path('categories/<int:id>/delete/', category_delete, name='category_delete'),

    # Participants
    path('participants/', participant_list, name='participant_list'),
    path('participants/add/', participant_create, name='participant_create'),
    path('participants/<int:id>/edit/', participant_update, name='participant_update'),
    path('participants/<int:id>/delete/', participant_delete, name='participant_delete'),

    # Search
    path('search/', search_events, name='search_events'),
]
