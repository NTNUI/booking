from django.db import models
from django.conf import settings
import datetime
import os


def get_thumbnail_upload_to(instance, filename):
    return os.path.join(
        "thumbnail/%s" % instance.slug, filename)


def get_cover_upload_to(instance, filename):
    return os.path.join(
        "cover_photo/%s" % instance.slug, filename)


class SportsGroup(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=12)
    description = models.TextField(max_length=200)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through='Membership', related_name='group_members')
    invitations = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through='Invitation', related_name='group_invitations')
    requests = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through='Request', related_name='group_requests')
    public = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to=get_thumbnail_upload_to, default='thumbnail/ntnui2.svg')
    cover_photo = models.ImageField(upload_to=get_cover_upload_to,
                                    default='cover_photo/ntnui-volleyball.png')

    def __str__(self):
        return self.name


class Board(models.Model):
    president = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='board_president')
    vice_president = models.ForeignKey(
        settings.AUTH_USER_MODEL,  related_name='board_vp')
    cashier = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='board_cashier')
    sports_group = models.OneToOneField(
        SportsGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "Board of NTNUI {}".format(self.sports_group.name)


class Membership(models.Model):
    person = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(SportsGroup, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.date.today)
    paid = models.BooleanField(default=False)
    in_board = models.BooleanField(default=False)
    role = models.CharField(max_length=30)


class Invitation(models.Model):
    person = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(SportsGroup, on_delete=models.CASCADE)
    date_issued = models.DateField(auto_now_add=True)


class Request(models.Model):
    person = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(SportsGroup, on_delete=models.CASCADE)
    date_issued = models.DateField(auto_now_add=True)
