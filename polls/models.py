"""
Copyright 2026 倪家诚（Jiacheng Ni）

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_text_en = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=280, blank=True)
    description_en = models.CharField(max_length=280, blank=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    @property
    def total_votes(self):
        return sum(choice.votes for choice in self.choice_set.all())

    @admin.display(boolean=True, ordering="pub_date", description="Published recently?")
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_text_en = models.CharField(max_length=200, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
