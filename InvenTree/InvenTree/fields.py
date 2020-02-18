""" Custom fields used in InvenTree """

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import validators
from django.db import models as models
from django.forms.fields import URLField as FormURLField

from .validators import allowable_url_schemes


class InvenTreeURLFormField(FormURLField):
    """ Custom URL form field with custom scheme validators """

    default_validators = [validators.URLValidator(schemes=allowable_url_schemes())]


class InvenTreeURLField(models.URLField):
    """ Custom URL field which has custom scheme validators """

    default_validators = [validators.URLValidator(schemes=allowable_url_schemes())]

    def formfield(self, **kwargs):
        return super().formfield(**{"form_class": InvenTreeURLFormField})
