#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State

@app_views.route('/states', strict_slashes=False)
def list_states():
    states = storage.all(State)
    return jsonify(
        [state.to_dict() for state in states.values()]
            )

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
