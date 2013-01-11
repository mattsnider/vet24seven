from django.db.models import fields
from django_shared.models import ModelBase

class CAMPAIGNS(object):
    NONE = 0
    BUDDY = 1

    CHOICES = (
        (BUDDY, 'buddy'),
        (NONE, 'n/a'),
    )

class MEDIUM(object):
    FORM = 1
    UNKNOWN = 0

    CHOICES = (
        (FORM, 'form'),
        (UNKNOWN, 'unknown'),
    )

class SOURCE(object):
    DIRECT = 1
    UNKNOWN = 0

    CHOICES = (
        (DIRECT, 'direct'),
        (UNKNOWN, 'unknown'),
    )


class EmailRecorder(ModelBase):
    campaign = fields.PositiveSmallIntegerField(choices=CAMPAIGNS.CHOICES)
    email = fields.EmailField(max_length=255)
    medium = fields.PositiveSmallIntegerField(choices=MEDIUM.CHOICES)
    source = fields.PositiveSmallIntegerField(choices=SOURCE.CHOICES)