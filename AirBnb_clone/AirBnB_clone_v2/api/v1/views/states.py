#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def list_states():
    states = storage.all(State)
    return jsonify(
        [state.to_dict() for state in states.values()]
            )

@app_views.route('/states',methods=['POST'], strict_slashes=False)
def create_state():
    data = request.get_json()
    if data is None:
        abort(404, "Not a JSON")
    if data.get("name") is None:
        abort(404, "Missing Name")
    new_state = State(**data)
    print(new_state)
    return jsonify(new_state.to_dict().get("name"))

@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(
        state.to_dict()
            )

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=True)
def delete_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    del state
    return jsonify({})
