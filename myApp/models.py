from django.db import models

class LoginAttempt(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} at {self.submitted_at.strftime('%Y-%m-%d %H:%M:%S')}"
