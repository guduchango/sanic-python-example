from sanic import Blueprint
from controllers.item_controller import (
    list_items, get_item, create_new_item, update_existing_item, delete_existing_item, test
)

item_bp = Blueprint("item_bp")

item_bp.route("/", methods=["GET"])(test)
item_bp.route("/items", methods=["GET"])(list_items)
item_bp.route("/items/<item_id:int>", methods=["GET"])(get_item)
item_bp.route("/items", methods=["POST"])(create_new_item)
item_bp.route("/items/<item_id:int>", methods=["PUT"])(update_existing_item)
item_bp.route("/items/<item_id:int>", methods=["DELETE"])(delete_existing_item)
