from marshmallow import fields

from remote.app import ma


class remote(ma.Schema):
    class Meta:
        fields = ("id", "time_stamb", "value")


remote_schema = remote()
