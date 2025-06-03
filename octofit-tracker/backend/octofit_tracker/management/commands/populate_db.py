from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User.objects.create(_id=ObjectId(), username="Superman", email="superman@example.com", password="password")
        user2 = User.objects.create(_id=ObjectId(), username="Batman", email="batman@example.com", password="password")

        # Create test teams
        team1 = Team.objects.create(_id=ObjectId(), name="Justice League")
        team1.members.add(user1, user2)

        # Create test activities
        activity1 = Activity.objects.create(_id=ObjectId(), user=user1, activity_type="Flying", duration=timedelta(hours=1))
        activity2 = Activity.objects.create(_id=ObjectId(), user=user2, activity_type="Martial Arts", duration=timedelta(hours=2))

        # Create test leaderboard entries
        leaderboard1 = Leaderboard.objects.create(_id=ObjectId(), user=user1, score=100)
        leaderboard2 = Leaderboard.objects.create(_id=ObjectId(), user=user2, score=200)

        # Create test workouts
        workout1 = Workout.objects.create(_id=ObjectId(), name="Strength Training", description="Lift heavy weights")
        workout2 = Workout.objects.create(_id=ObjectId(), name="Endurance Training", description="Run long distances")

        self.stdout.write(self.style.SUCCESS('Test data populated successfully'))
