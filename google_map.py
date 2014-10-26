#!/usr/bin/env python
# coding=utf-8

import flask
import test
import json
from flask import Flask
from flask import render_template, session, request

app = Flask(__name__)
app.debug = True
app.secret_key='this key is very secret indeed'

@app.route('/')

@app.route('/complexshow')
def complexshow(name=None):
    array = test.get_cluster()

    args = {
            #'cluster_num': num,
            'cluster': json.dumps(array)
            };

    return render_template('complexshow.html', name=name, **args)

@app.route('/get_clusters')
def get_clusters():
    array = test.get_cluster()

    return flask.jsonify( {'clusters': array} )

@app.route('/mapshow')
def mapshow(name=None):
    # Render the cluster on Google Map
    return render_template('mapshow.html', name=name)

if __name__ == '__main__':
    app.run()
