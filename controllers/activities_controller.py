from flask import Flask, Blueprint, redirect, render_template, request, url_for

from models.activity import Activity
from models.location import Location
import repositories.activity_repo as act_repo

act_bp = Blueprint("activities", __name__)

#add
@act_bp.route("activities/add")
