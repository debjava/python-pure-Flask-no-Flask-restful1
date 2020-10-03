from flask import Flask

from webapp.resources.DeleteApi import deleteAPI
from webapp.resources.FileDownloadAPI import fileDownloadAPI
from webapp.resources.FileUploadAPI import fileUploadAPI
from webapp.resources.GetAPI import getAPI
from webapp.resources.PatchAPI import patchAPI
from webapp.resources.PostAPI import postAPI
from webapp.resources.PutAPI import putAPI

app = Flask(__name__)

app.register_blueprint(getAPI)
app.register_blueprint(postAPI)
app.register_blueprint(putAPI)
app.register_blueprint(patchAPI)
app.register_blueprint(deleteAPI)
app.register_blueprint(fileUploadAPI)
app.register_blueprint(fileDownloadAPI)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)  # Using Flask only
