"""Application routes."""
from flask import render_template, request, redirect, url_for, jsonify, abort
from flask import current_app as app
from .models import db


@app.route("/", methods=['GET'])
def home():	
	return render_template('index.html', title="Some Title")

# Write routes

