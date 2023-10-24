# @bp.route('/update/item/')
# @limiter.limit(rate_limit_from_user, override_defaults=True)
# def api_update_item():
#     if len(request.args) == 3 and 'mat_id' in request.args and 'new_title' in request.args and 'new_material_type' in request.args:
#         mat_id = request.args.get('mat_id', None)
#         _new_title = request.args.get('new_title', None)
#         _new_material_type = request.args.get('new_material_type', None)
#         status_code = update_item(mat_id, _new_title, _new_material_type)
#         print("status code was:", status_code)
#         if status_code == 201:
#             return jsonify({'updated': mat_id}), 201
#         else: return 500
#     else: abort(404)