import helper
import time
import os
from flask import send_file
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from config import FILES_FOLDER, ALLOWED_EXTENSIONS
from db.data_storage import DataStorage


class FileManager(Resource):
    def get(self, id):
        result = DataStorage.update_file(_id=id)
        if result:
            return 'Ok', 200
        return 'File not found', 404


class UploadedFile(Resource):
    def get(self, link):
        file = DataStorage.get_by_link(link=link)
        if file:
            if int(file.expire_at) < int(time.time()):
                return 'Link is expired', 404

            full_path = os.path.join(FILES_FOLDER, file.filename)
            if os.path.exists(full_path):
                return send_file(full_path, as_attachment=True)
            else:
                return 'File is removed', 404
        return 'File not found', 404


class Upload(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('files', type=FileStorage, location='files')
        data = parser.parse_args()

        if not data['files']:
            return 'File not found', 404
        file = data['files']

        if file:
            extensions = str(file.filename).split('.')
            extension = extensions[len(extensions)-1]
            if extension not in ALLOWED_EXTENSIONS:
                return 'Bad extension', 404

            link = helper.generate_unique_filename(filename=file.filename)
            filename = '%s.%s' % (link, extension)
            file_path = os.path.join(FILES_FOLDER, filename)
            try:
                file.save(file_path)
                my_file = DataStorage.create_file(filename=filename)
                if my_file:
                    return {'id': my_file.id, 'link': my_file.link}
                return 'All good', 200
            except Exception as e:
                print(e)
                return 'File not uploaded', 404
        return 'File not uploaded', 404
