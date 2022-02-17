from subprocess import call
from flask import Blueprint
from controllers.invocation_controller import invoke

invocation_blueprint = Blueprint('invocation', __name__)

invocation_blueprint.route('/<string:url>', methods=['GET'])(invoke)