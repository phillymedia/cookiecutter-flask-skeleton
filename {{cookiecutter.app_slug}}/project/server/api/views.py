# project/server/user/views.py


from flask import Blueprint, url_for, redirect, request
from flask_login import login_user, logout_user, login_required
from flask_json import json_response

from project.server import bcrypt, db

from datetime import datetime

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/", methods=["GET", "POST"])
def index():

    return json_response(time=datetime.utcnow())



@api_blueprint.route("/members")
@login_required
def members():
    
    return json_response(time=datetime.utcnow())
