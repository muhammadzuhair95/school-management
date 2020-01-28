from django.db import models


# Create your models here.
class Course(models.Model):
    """ Database Model for Course/Classes held in school"""

    subject_name = models.CharField(blank=False, max_length=50)
    subject_description = models.CharField(blank=True, max_length=150)
    subject_fee = models.PositiveIntegerField(default=0)
 
    def __str__(self):
        return self.subject_name

    def __repr__(self):
        return 'Course : ' + self.subject_name
