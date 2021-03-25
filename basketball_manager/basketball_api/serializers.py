# api <json>
from rest_framework import serializers
from .models import Team, Player, User, Match, Round, Tournament
from rest_framework.fields import ReadOnlyField
import logging

logger = logging.getLogger(__name__)


class BkUserSerializer(serializers.ModelSerializer):
    logger.info('Starting user serializer!')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserSerializer(serializers.ModelSerializer):
    logger.info('Starting user serializer!')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'no_of_logins', 'total_time_spent']


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    logger.info('Starting team serializer!')
    avg_team_score = ReadOnlyField(source='get_avg_team_score', default=0)

    class Meta:
        model = Team
        fields = ['id','name', 'address', 'mobile', 'created_at', 'avg_team_score']


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    logger.info('Starting Tournament serializer!')
    class Meta:
        model = Tournament
        fields = '__all__'


class RoundSerializer(serializers.HyperlinkedModelSerializer):
    logger.info('Starting round serializer!')
    tournament = TournamentSerializer()

    class Meta:
        model = Round
        fields = ['id', 'round', 'created_at', 'tournament']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    logger.info('Starting player serializer!')
    team = TeamSerializer()
    avg_score = ReadOnlyField(source='get_stats', default=0)
    no_of_matches = ReadOnlyField(source='get_no_of_matches', default=0)
    players_type = ReadOnlyField(source='get_player_type', default=0)

    class Meta:
        model = Player
        fields = ['id', 'fullname', 'height', 'team', 'avg_score', 'no_of_matches', 'players_type']


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    logger.info('Starting Match serializer!')
    winning_team = TeamSerializer()
    losing_team = TeamSerializer()
    round = RoundSerializer()

    class Meta:
        model = Match
        fields = ['winning_team', 'losing_team', 'winning_team_score', 'losing_team_score', 'round']
