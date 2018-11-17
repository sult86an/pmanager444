from django.urls import path
from . import pviews
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = 'pmanager'
urlpatterns = [
    # /initiatives/

    path('user_login/', pviews.user_login, name='user'),
    path('logout/', pviews.user_logout, name='logout'),
    path('home/', pviews.IndexView.as_view(), name='home'),
    path('initiative/', pviews.InitiativesView.as_view(), name='initiative'),
    path('goals/<int:id>/', pviews.GoalsView.as_view(), name='goals'),
    path('supports/<int:id>/', pviews.SupportsView.as_view(), name='supports'),
    path('Risks/<int:id>/', pviews.RisksView.as_view(), name='risks'),
    path('challenges/<int:id>/', pviews.ChallengesView.as_view(), name='challenges'),
    path('stages/<int:id>/', pviews.StagesView.as_view(), name='stages'),
    path('reports/<int:id>/', pviews.ListWeek.as_view(), name='reports'),
    path('reports/<int:id>/<week_no>/<int:pk>/', pviews.DetailView.as_view(), name='details'),
    path('leaders/', pviews.LeadersView.as_view(), name='leaders'),
    path('messages/', pviews.EnqueryView.as_view(), name='messages'),



]

