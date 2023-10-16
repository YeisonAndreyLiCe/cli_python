import peewee
import os

DATABASE = peewee.MySQLDatabase(
    "weibnarcf",
    user=os.environ.get("MYSQL_USER"),
    passwd=os.environ.get("MYSQL_ROOT_PASSWORD"),
    host=os.environ.get("MYSQL_HOST"),
    port=os.environ.get("MYSQL_PORT"),
)


class User(peewee.Model):
    username = peewee.CharField(max_length=50, unique=True, null=False)
    email = peewee.CharField(max_length=50, unique=True, null=False)
    password = peewee.CharField(max_length=50, null=False)
    active = peewee.BooleanField(default=True)

    class Meta:
        database = DATABASE
        db_table = "users"

    def __str__(self):
        return self.username


MODELS = [User]
