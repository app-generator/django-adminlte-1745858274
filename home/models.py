# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    designation = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Organization(models.Model):

    #__Organization_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    isactive = models.BooleanField()

    #__Organization_FIELDS__END

    class Meta:
        verbose_name        = _("Organization")
        verbose_name_plural = _("Organization")


class Chartofaccounts(models.Model):

    #__Chartofaccounts_FIELDS__
    coaid = models.IntegerField(null=True, blank=True)
    orgid = models.ForeignKey(Organization, on_delete=models.CASCADE)
    coa = models.TextField(max_length=255, null=True, blank=True)

    #__Chartofaccounts_FIELDS__END

    class Meta:
        verbose_name        = _("Chartofaccounts")
        verbose_name_plural = _("Chartofaccounts")



#__MODELS__END
