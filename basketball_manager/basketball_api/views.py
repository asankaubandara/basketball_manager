from rest_framework import viewsets
from . import models
from . import serializers


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeamSerializer
    queryset = models.Team.objects.all()


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlayerSerializer
    queryset = models.Player.objects.all()


class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MatchSerializer
    queryset = models.Match.objects.all()


class RoundViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RoundSerializer
    queryset = models.Round.objects.all()


class TournamentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TournamentSerializer
    queryset = models.Tournament.objects.all()
