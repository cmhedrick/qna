from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    org_logo = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile/%Y/%m/%d'
    )
    phone_number = models.CharField(
        max_length=12,
        default='XXXXXXXXXX'
    )
    org_name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default="organization name"
    )

    def __unicode__(self):
        return "%s" % (self.org_name)

    def __str__(self):
        return "%s" % (self.org_name)


class Role(models.Model):
    role = models.CharField(
        max_length=32,
        blank=False,
        null=False,
        default="role"
    )

    def __unicode__(self):
        return "%s" % (self.role)

    def __str__(self):
        return "%s" % (self.role)


class Staff(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="staff",
        null=True
    )
    role = models.ManyToManyField(Role)
    org = models.ManyToManyField(Organization)
    profile_pic = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile/%Y/%m/%d'
        )
    phone_number = models.CharField(
        max_length=12,
        default='XXXXXXXXXX'
    )

    @property
    def email(self):
        return self.user.email

    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Question(models.Model):
    user = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name="questions",
        null=True
    )
    org = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    question = models.TextField()
    answer = models.TextField()

    @property
    def is_answered(self):
        return bool(self.answer)

    def __unicode__(self):
        return "%s: %s" % (self.org.org_name, self.question[:15])

    def __str__(self):
        return "%s: %s" % (self.org.org_name, self.question[:15])
