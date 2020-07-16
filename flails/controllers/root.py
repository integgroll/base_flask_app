from flask import Blueprint, render_template

part = Blueprint("root_controller",__name__)

@part.route("/")
def homepage():
    return """Flask App that 'Works' like Integgroll's brain"""