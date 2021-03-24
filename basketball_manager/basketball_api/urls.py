from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('team', viewset=views.TeamViewset)
router.register('team_player', viewset=views.PlayerViewset)
router.register('match', viewset=views.MatchViewset)
router.register('round', viewset=views.RoundViewset)
router.register('tournament', viewset=views.Tournamentiewset)

urlpatterns = [
    path('', include(router.urls))
]