from flask import request, jsonify
from functools import wraps

_TOOL_HANDLERS = {}
docs_api = drive_api = None

def register_tool(route: str):
    def decorator(fn):
        _TOOL_HANDLERS[route] = fn
        return fn
    return decorator

def attach_routes(app):
    for route, fn in _TOOL_HANDLERS.items():
        @app.route(route, methods=["POST"])
        @wraps(fn)
        def handler(fn=fn):
            try:
                return jsonify(fn(request.get_json() or {}))
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        handler.__name__ = f"handler_{route.replace('/', '_')}"