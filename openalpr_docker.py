#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
import json
from flask import Flask, jsonify, request, abort, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

conf = {
  "path_download":"/var/www/uploads/"
}

def getLicensePlateNumber(path, filename):
	command = f'sudo docker run -it --rm -v {path}:/data:ro openalpr -c eu -j {filename}'
	try:
		return json.loads(os.popen(command).read())["results"][0]["plate"]
	except:
		return ''

@app.route('/ocr', methods=['POST'])
def upload_file():  
  f = request.files['picture_car']
  f.save(f'{conf["path_download"]}{secure_filename(f.filename)}')
  res = getLicensePlateNumber(conf["path_download"],secure_filename(f.filename))
  os.remove(f'{conf["path_download"]}{secure_filename(f.filename)}')
  return res
