from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models

'''
class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        question = models.TextField()
        option_one = models.CharField(max_length=50)
        option_two = models.CharField(max_length=50)
        option_three = models.CharField(max_length=50)

        # options = ArrayField(models.CharField(max_length=70))
        # options_count = ArrayField(models.IntegerField(default=0))

        option_one_count = models.IntegerField(default=0)
        option_two_count = models.IntegerField(default=0)
        option_three_count = models.IntegerField(default=0)

        option_one_percent = int((option_one_count / self.total()) * 100) if self.total() > 0 else 0
        option_two_percent = int((option_two_count / self.total()) * 100) if self.total() > 0 else 0
        option_three_percent = int((option_three_count / self.total()) * 100) if self.total() > 0 else 0

    # creation_date = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    # def percent_for_option(self, option_index):
    #     try:
    #         return int((self.options_count[option_index] / self.total()) * 100)
    #     except (ZeroDivisionError, IndexError):
    #         return 0

'''


class Poll(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('single', 'Single Choice'),
        ('multiple', 'Multiple Choice'),
    ]

    question = models.TextField()
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    time = models.DateTimeField(default=now)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPE_CHOICES, default='single')

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    @property
    def option_one_percent(self):
        return int((self.option_one_count / self.total()) * 100) if self.total() > 0 else 0

    @property
    def option_two_percent(self):
        return int((self.option_two_count / self.total()) * 100) if self.total() > 0 else 0

    @property
    def option_three_percent(self):
        return int((self.option_three_count / self.total()) * 100) if self.total() > 0 else 0
