from flask import render_template
from python_framework import ResourceManager
import ModelAssociation


app = ResourceManager.initialize(__name__, ModelAssociation.MODEL)


@app.route(f'{app.api.baseUrl}')
def home():
    return render_template('index.html', staticUrl=ResourceManager.getApiStaticUrl(app))
