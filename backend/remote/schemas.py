from marshmallow import fields

from itlhole.app import ma


class Random(ma.Schema):
    class Meta:
        fields = ("id", "time_stamb", "value")


random_schema = Random()
