from rest_framework import viewsets
from . import models
from . import serializers


class TeamViewset(viewsets.ModelViewSet):
    serializer_class = serializers.TeamSerializer
    queryset = models.Team.objects.all()


class PlayerViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PlayerSerializer
    queryset = models.Player.objects.all()


class MatchViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MatchSerializer
    queryset = models.Match.objects.all()


class RoundViewset(viewsets.ModelViewSet):
    serializer_class = serializers.RoundSerializer
    queryset = models.Round.objects.all()


class Tournamentiewset(viewsets.ModelViewSet):
    serializer_class = serializers.TournamentSerializer
    queryset = models.Tournament.objects.all()
