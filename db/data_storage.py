import time
import peewee
from db.models import File, database
from helper import generate_unique_link
from config import LINK_LIFE_TIME


class DataStorage:

    @classmethod
    def get_by_id(cls, _id):
        try:
            file = File.get(id=_id)
        except peewee.DoesNotExist:
            return None
        return file

    @classmethod
    def get_by_link(cls, link):
        try:
            file = File.get(link=link)
        except peewee.DoesNotExist:
            return None
        return file

    @classmethod
    def create_file(cls, filename):
        with database.atomic():
            try:
                file = File()
                file.filename = filename
                file.link = generate_unique_link()
                file.expire_at = int(time.time()) + LINK_LIFE_TIME
                file.save()
                return file
            except Exception as e:
                print(e)
                database.rollback()
        return False

    @classmethod
    def update_file(cls, _id):
        update = {}
        update['expire_at'] = int(time.time()) + LINK_LIFE_TIME
        with database.atomic():
            try:
                File.update(update).where(File.id == _id).execute()
                return update['expire_at']
            except Exception as e:
                print(e)
                database.rollback()
        return False
