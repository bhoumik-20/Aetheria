from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    
    # AI Analysis Results (we'll populate these later)
    dominant_colors = models.JSONField(default=list, blank=True)
    detected_style = models.CharField(max_length=100, blank=True)
    style_confidence = models.FloatField(null=True, blank=True)
    analysis_completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"
    
    def get_absolute_url(self):
        return reverse('board_detail', kwargs={'pk': self.pk})

class BoardImage(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='board_images/')
    original_filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # AI Analysis Results for individual images (we'll populate these later)
    dominant_colors = models.JSONField(default=list, blank=True)
    detected_objects = models.JSONField(default=list, blank=True)
    analysis_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.original_filename} in {self.board.title}"
