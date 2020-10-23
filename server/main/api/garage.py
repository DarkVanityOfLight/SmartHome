# -*- coding: utf-8 -*-
"""Api for opening/closing and status of garage"""
from flask import Blueprint, jsonify

route = Blueprint('garage', __name__)

# True means open, False is closed
status = False

@app.route("/open")
def open():
    status = True
    return jsonify({"status": 200, "open": status})

@app.route("/close")
def close():
    status = False
    return jsonify({"status": 200, "closed": status})


@app.route("/status")
def status():
    return jsonify("status": 200, "stat": status)