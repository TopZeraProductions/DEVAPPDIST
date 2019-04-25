from flask import Blueprint, request, jsonify, Response

todo_api = Blueprint('todo_api', __name__, template_folder='templates')
