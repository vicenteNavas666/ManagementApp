from django.utils import timezone
from django.db import models

# Create your models here.

class Projects(models.Model):
    PKProject = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=20)  
    Description = models.TextField()
    StartDate = models.DateField(default=timezone.now)  # autoset to current date
    EndDate = models.DateField()                           
    Status = models.CharField(max_length=20, default='Pending')  
    Priority = models.CharField(
        max_length=20,
        choices=[
            ('LOW', 'Low'),
            ('MEDIUM', 'Medium'),
            ('HIGH', 'High')
        ])

    def __str__(self):  # value to return when casted to str()
        return self.Title

class Tasks(models.Model):
    FKProject = models.ForeignKey(Projects, on_delete=models.CASCADE)
    Title = models.CharField(max_length=20) 
    Description = models.TextField()
    StartDate = models.DateField()  
    EndDate = models.DateField()     

    def save(self):
        self.FKProject.EndDate = max(self.FKProject.EndDate, self.EndDate)
        super().save()

    def __str__(self):
        return self.Title

class Personnel(models.Model):
    FKProject = models.ForeignKey(Projects, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    Role = models.CharField(max_length=20)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Name} {self.Surname}"                                                                                # Concatenate Name and Surname
