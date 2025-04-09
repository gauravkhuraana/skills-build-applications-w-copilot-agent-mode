from django.core.management.base import BaseCommand
from pymongo import MongoClient
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Populate users
        db.users.drop()  # Clear existing data
        db.users.insert_many(test_users)

        # Populate teams
        db.teams.drop()
        db.teams.insert_many(test_teams)

        # Populate activities
        db.activities.drop()
        db.activities.insert_many(test_activities)

        # Populate leaderboard
        db.leaderboard.drop()
        db.leaderboard.insert_many(test_leaderboard)

        # Populate workouts
        db.workouts.drop()
        db.workouts.insert_many(test_workouts)

        self.stdout.write(self.style.SUCCESS('Database populated successfully with test data.'))
