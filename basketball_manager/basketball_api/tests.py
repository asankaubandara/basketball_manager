from django.test import TestCase

import uuid
from basketball_manager.basketball_api.models import Team

# Create your tests here.

"""
Due to the below errors couldn't verify the test class, because of that i just wrote only for one model
django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. 
You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() 
before accessing settings.
"""


def _create_team(name, address,
                 mobile):
    team_id = uuid.uuid4()
    team = Team(id=team_id, name=name,
                address=address, mobile=mobile)
    return team


class TeamModelTest(TestCase):
    def test_team_create(self):
        name = "Greatest team ever"
        address = "Team Address"
        mobile = "+94777123456"
        team_id, team = _create_team(name, address,
                                     mobile)
        self.assertEqual(team_id, team.team_id)
        self.assertEqual(name, team.name)
        self.assertEqual(address, team.address)
        self.assertEqual(mobile, team.mobile)
        # Note: a test/assert related to many to many field 'Team' has been
        # skipped
