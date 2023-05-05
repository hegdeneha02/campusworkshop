"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaas73hp8u791h19sc0-a.oregon-postgres.render.com",
        database="todo_ntr5",
        user="todo_nt5r_user",
        password="bb0GjkIS3fEslcUFaUj3m6In6Qa36qMF")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
