from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=20)
    viewpassword=models.CharField(max_length=20)
class Register(models.Model):
    Name=models.CharField(max_length=40,null=True)
    Address=models.CharField(max_length=40,null=True)
    Email=models.CharField(max_length=40,null=True)
    Phone=models.CharField(max_length=40,null=True)
    usertype=models.CharField(max_length=40,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class AdminMovie(models.Model):
    # Defining the specific emotions as constants
    EMOTION_CHOICES = [
        ('angry', 'Angry'),
        ('fear', 'Fear'),
        ('happy', 'Happy'),
        ('neutral', 'Neutral'),
        ('sad', 'Sad'),
        ('surprise', 'Surprise'),
    ]

    movie_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='admin_movies/', null=True, blank=True)
    movie_link = models.URLField(max_length=500)

    # Emotion categorization
    emotion_type = models.CharField(
        max_length=20,
        choices=EMOTION_CHOICES,
        default='neutral'
    )

    # Star Rating (0.0 to 5.0)
    star_rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )

    def __str__(self):
        return f"{self.movie_name} ({self.emotion_type})"

class Feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
