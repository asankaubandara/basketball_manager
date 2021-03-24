from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('team', viewset=views.TeamViewSet)
router.register('team_player', viewset=views.PlayerViewSet)
router.register('match', viewset=views.MatchViewSet)
router.register('round', viewset=views.RoundViewSet)
router.register('tournament', viewset=views.TournamentViewSet)

urlpatterns = [
    path('', include(router.urls))
]