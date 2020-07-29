#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from flask import Flask, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', method=['POST', 'GET'])
def upload(request):
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'static', 'upload', secure_filename(f.filename))
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('index.html')
