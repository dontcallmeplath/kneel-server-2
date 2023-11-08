import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_create, db_delete


class OrdersView:
    def get(self, handler, url):
        sql = """SELECT o.id, o.metal_id, o.style_id, o.size_id FROM `Order` o"""
        if url["pk"] != 0:
            sql += " WHERE o.id = ?"
            query_results = db_get_single(sql, url["pk"])
            diction_order = dict(query_results)
            if "_expand" in url["query_params"] and "metal" in url["query_params"]["_expand"]:
                metal_fk = diction_order["metal_id"]
                metal_sql = """SELECT m.id, m.metal, m.price FROM Metal m WHERE m.id = ?"""
                metal_info = db_get_single(metal_sql, metal_fk)
                metal_object = {
                    "id": metal_info["id"],
                    "metal": metal_info["metal"],
                    "price": metal_info["price"]
                }
                diction_order["metal"] = metal_object
            if "_expand" in url["query_params"] and "style" in url["query_params"]["_expand"]:
                style_fk = diction_order["style_id"]
                style_sql = """SELECT s.id, s.style, s.price FROM Style s WHERE s.id = ?"""
                style_info = db_get_single(style_sql, style_fk)
                style_object = {
                    "id": style_info["id"],
                    "style": style_info["style"],
                    "price": style_info["price"]
                }
                diction_order["style"] = style_object
            if "_expand" in url["query_params"] and "size" in url["query_params"]["_expand"]:
                size_fk = diction_order["size_id"]
                size_sql = """SELECT s.id, s.caret, s.price FROM Size s WHERE s.id = ?"""
                size_info = db_get_single(size_sql, size_fk)
                size_object = {
                    "id": size_info["id"],
                    "caret": size_info["caret"],
                    "price": size_info["price"]
                }
                diction_order["size"] = size_object

            serialized_order = json.dumps(diction_order)
            return handler.response(serialized_order, status.HTTP_200_SUCCESS.value)
        else:
            sql = """SELECT o.id, o.timestamp, o.metal_id, o.style_id, o.size_id FROM `Order` o """
            query_results = db_get_all(sql)
            orders = [dict(row) for row in query_results]
            serialized_orders = json.dumps(orders)
            return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)


    def delete(self, handler, pk):
        number_of_rows_deleted = db_delete("DELETE FROM `Order` WHERE id = ?", pk)

        if number_of_rows_deleted > 0:
            return handler.response("Order has been deleted", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response(
                "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )

    def post(self, handler, order_data):
        sql = """
        INSERT INTO `Order`(metal_id, style_id, size_id) VALUES (?, ?, ?);
        """
        added_order = db_create(
            sql, (order_data["metal_id"], order_data["style_id"], order_data["size_id"])
        )
        order = {
            "id": added_order,
            "metal_id": order_data["metal_id"],
            "style_id": order_data["style_id"],
            "size_id": order_data["size_id"],
        }
        serialized_order = json.dumps(order)

        if added_order:
            return handler.response(
                serialized_order, status.HTTP_201_SUCCESS_CREATED.value
            )
        else:
            return handler.response(
                "", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value
            )
