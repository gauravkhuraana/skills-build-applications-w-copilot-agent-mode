from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Test data for users
        users = [
            {"username": "john_doe", "email": "john@example.com", "password": "password123"},
            {"username": "jane_smith", "email": "jane@example.com", "password": "password123"}
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": [users[0]["_id"]]},
            {"name": "Team Beta", "members": [users[1]["_id"]]}
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user": users[0]["_id"], "activity_type": "running", "duration": 30},
            {"user": users[1]["_id"], "activity_type": "walking", "duration": 45}
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"user": users[0]["_id"], "score": 100},
            {"user": users[1]["_id"], "score": 80}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Morning Run", "description": "A quick 5km run to start the day."},
            {"name": "Evening Yoga", "description": "Relaxing yoga session to wind down."}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
