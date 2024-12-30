from django.db import models
from django.contrib.auth.models import User

# 1. User Table
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_deaf = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# 2. Content Table
class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content_type = models.CharField(max_length=50, choices=(('Article', 'Article'), ('Video', 'Video')))
    video_caption_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 3. Resource Table
class Resource(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    resource_url = models.URLField()
    video = models.FileField(upload_to='videos/', default='default_video.mp4')  # Default video

    def __str__(self):
        return self.name


# 4. Event Table
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    organizer = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# 5. Feedback Table
class Feedback(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, null=True, blank=True)
    feedback_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Ratings from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.user.username} - Rating: {self.rating}"
