from flask import Blueprint, request, jsonify, Response

todo_api = Blueprint(
    'TodoApi',
    __name__,
    template_folder='templates'
)
