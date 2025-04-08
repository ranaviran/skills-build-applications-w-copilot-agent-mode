from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "Thor", "created_at": datetime.now()},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "Tony Stark", "created_at": datetime.now()},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "Steve Rogers", "created_at": datetime.now()},
            {"_id": ObjectId(), "email": "crashoverride@mhigh.edu", "name": "Natasha Romanoff", "created_at": datetime.now()},
            {"_id": ObjectId(), "email": "sleeptoken@mhigh.edu", "name": "Bruce Banner", "created_at": datetime.now()},
        ]
        db.users.insert_many(users)

        # Insert teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"], users[2]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Insert activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "type": "Cycling", "duration": 60, "date": "2025-04-01"},
            {"_id": ObjectId(), "user": users[1]["_id"], "type": "Crossfit", "duration": 120, "date": "2025-04-02"},
            {"_id": ObjectId(), "user": users[2]["_id"], "type": "Running", "duration": 90, "date": "2025-04-03"},
            {"_id": ObjectId(), "user": users[3]["_id"], "type": "Strength", "duration": 30, "date": "2025-04-04"},
            {"_id": ObjectId(), "user": users[4]["_id"], "type": "Swimming", "duration": 75, "date": "2025-04-05"},
        ]
        db.activity.insert_many(activities)

        # Insert leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "team": teams[0]["_id"], "score": 300},
            {"_id": ObjectId(), "team": teams[1]["_id"], "score": 250},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Insert workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
