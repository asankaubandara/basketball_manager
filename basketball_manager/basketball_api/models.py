from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg
from django.utils.timezone import now


# Create your models here.

class User(AbstractUser, models.Model):
    user_type = models.IntegerField(default=0)
    no_of_logins = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Team(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_avg_team_score(self):
        total_score = PlayerStats.objects.filter(team_id=self.id).aggregate(avg_score=Avg('score'))['avg_score']
        no_of_games = PlayerStats.objects.values('match_id').filter(team_id=self.id).distinct().count()
        return total_score / no_of_games


class Player(models.Model):
    fullname = models.CharField(max_length=100)
    player_type = models.IntegerField(default=0)
    height = models.FloatField(max_length=15)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)

    @property
    def get_stats(self):
        return self.stats.aggregate(avg_score=Avg('score'))['avg_score']

    @property
    def get_player_type(self):
        status = self.player_type
        if self.player_type == 1:
            status = 'Player'
        else:
            status = 'Coach'
        return status

    @property
    def get_no_of_matches(self):
        return PlayerStats.objects.values('match_id').filter(player_id=self.id).distinct().count()


class Tournament(models.Model):
    name = models.TextField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(default=now)


class Round(models.Model):
    round = models.IntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class Match(models.Model):
    round = models.ForeignKey(Round, on_delete=models.DO_NOTHING)
    winning_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="winning_team")
    losing_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="losing_team")
    winning_team_score = models.IntegerField(default=0)
    losing_team_score = models.IntegerField(default=0)
    game_date = models.DateTimeField()
    player_stats = models.ManyToManyField(Player, through='PlayerStats')


class PlayerStats(models.Model):
    score = models.IntegerField()
    match = models.ForeignKey(Match, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING, related_name='stats')
