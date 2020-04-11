from marshmallow import fields

from remote.app import ma


class random(ma.Schema):
    class Meta:
        fields = ("id", "time_stamb", "value")


random_schema = random()
