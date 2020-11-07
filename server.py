from flask import Flask
from flask_restful import Api
from upload import FileManager, Upload, UploadedFile
from config import SECRET_KEY

app = Flask(__name__)
api = Api(app)

app.config['CORS_HEADERS'] = 'application/json'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 mb max


api.add_resource(Upload, '/upload')
api.add_resource(UploadedFile, '/<string:link>')
api.add_resource(FileManager, '/fm/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
