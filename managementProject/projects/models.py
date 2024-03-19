from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Projects(models.Model):
    PKProjectID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=20)  
    Description = models.TextField()
    StartDate = models.DateField(default=timezone.now)                                                                      #autoset to current date
    EndDate = models.DateField()                           
    Status = models.CharField(max_length=20, default='Pending')  
    Priority = models.CharField(max_length=20,
    choices=[
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High')
    ])

    def clean(self):
        if self.EndDate < self.StartDate:                                                                                   #EndDate must be greater or equal to StartDate
            raise ValidationError("End Date must be greater than or equal to Start Date.")

    def __str__(self):                                                                                                      #value to return when casted to str()
        return self.Title

class Tasks(models.Model):
    FKProjectID = models.ForeignKey(Projects, on_delete=models.CASCADE)                                                     #delete all tasks upon project deletion
    Title = models.CharField(max_length=20) 
    Description = models.TextField()
    StartDate = models.DateField(validators=[MinValueValidator(limit_value=models.F('FKProjectID__StartDate'))])            #task StartDate must be greater or equal to project StartDate
    EndDate = models.DateField(validators=[MinValueValidator(limit_value=models.F('StartDate'))])                           

    def save(self):                                                                                                         #if task EndDate is greater than project EndDate, update it
        self.FKProjectID.EndDate = max(self.FKProjectID.EndDate, self.EndDate)
        super().save()

    def __str__(self):
        return self.Title

class Personnel(models.Model):
    FKProjectID = models.ForeignKey(Projects, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    Role = models.CharField(max_length=20)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Name} {self.Surname}"                                                                                # Concatenate Name and Surname
