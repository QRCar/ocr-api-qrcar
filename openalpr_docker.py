#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
import json
from flask import Flask, jsonify, request, abort, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)



def getLicensePlateNumber(path, filename):
	command = f'sudo docker run -it --rm -v {path}:/data:ro openalpr -c eu -j {filename}'
	try:
		return json.loads(os.popen(command).read())["results"][0]["plate"]
	except:
		return ''

@app.route('/ocr', methods=['POST'])
def upload_file():  
  path_upload="/var/www/uploads/"
  f = request.files['picture_car']
  f.save(f'{path_upload}{secure_filename(f.filename)}')
  res = getLicensePlateNumber(path_upload,secure_filename(f.filename))
  os.remove(f'{path_upload}{secure_filename(f.filename)}')
  return res

conf = {"host":"0.0.0.0","port":5000}
app.run(**conf)
