from db.base import database_setting
import peewee
import time

database = database_setting()


class File(peewee.Model):
    filename = peewee.CharField(max_length=255, verbose_name='filename', null=False)
    link = peewee.CharField(max_length=255, verbose_name='link', default='', null=False, unique=True)
    expire_at = peewee.IntegerField(verbose_name='expire', default=int(time.time()))

    class Meta:
        verbose_name = 'Files'
        verbose_name_plural = 'Files'
        db_table = 'files'
        database = database

    def __str__(self):
        return "File(%s %s)" % (self.filename, self.link)


database.create_tables([
    File
])
