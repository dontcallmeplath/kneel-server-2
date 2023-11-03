import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all

class SizesView():

    def get(self, handler, url):
        pk = url['pk']
        if pk != 0:
            sql = """ SELECT s.id, s.caret, s.price FROM Size s WHERE s.id = ?"""
            query_results = db_get_single(sql, pk)
            serialized_size = json.dumps(dict(query_results))
            return handler.response(serialized_size, status.HTTP_200_SUCCESS.value)
        else:
            sql = """SELECT s.id, s.caret, s.price FROM Size s"""
            query_results = db_get_all(sql)
            sizes = [dict(row) for row in query_results]
            serialized_sizes = json.dumps(sizes)
            return handler.response(serialized_sizes, status.HTTP_200_SUCCESS.value)
