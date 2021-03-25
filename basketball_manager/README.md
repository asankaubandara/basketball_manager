# Basketball Match Manager System

A Basketball teams, players, matches and ratings app

This is a Django based project. The models, and tests have been written as per the framework.

A couple of migrations scripts have been provided to setup the tables.

Admin panel has access to all models so this app can be tested using some sample data creation there too.

Tests have been included for one models, due to a error couldn't run it.

Python Version : 3.9.2


To run the application:
python manage.py runserver


To access the apis (for example on localhost):
  * api list page: http://127.0.0.1:8000/api/
  * teams list: http://127.0.0.1:8000/api/team/
  * team detail: http://127.0.0.1:8000/api/team/<id>
  * match list: http://127.0.0.1:8000/api/match/
  * match detail: http://127.0.0.1:8000/api/match/<id>
  * team players list: http://127.0.0.1:8000/api/team_player/
  * team players detail: http://127.0.0.1:8000/api/team_player/<id>
  * tournaments list: http://127.0.0.1:8000/api/tournament/
  * tournament detail: http://127.0.0.1:8000/api/tournament/<id>
