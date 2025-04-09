from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"]]},
            {"name": "Gold Team", "members": [users[2]["_id"], users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user": users[0]["_id"], "activity_type": "Cycling", "duration": 60},
            {"user": users[1]["_id"], "activity_type": "Crossfit", "duration": 120},
            {"user": users[2]["_id"], "activity_type": "Running", "duration": 90},
            {"user": users[3]["_id"], "activity_type": "Strength", "duration": 30},
            {"user": users[4]["_id"], "activity_type": "Swimming", "duration": 75},
        ]
        db.activities.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"user": users[0]["_id"], "score": 100},
            {"user": users[1]["_id"], "score": 90},
            {"user": users[2]["_id"], "score": 95},
            {"user": users[3]["_id"], "score": 85},
            {"user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Cycling Training", "description": "Training for a road cycling event"},
            {"name": "Crossfit", "description": "Training for a crossfit competition"},
            {"name": "Running Training", "description": "Training for a marathon"},
            {"name": "Strength Training", "description": "Training for strength"},
            {"name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
