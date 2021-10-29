import sqlite3 as mdb
from bottle import FormsDict
from hashlib import md5
import os
import time
from argon2 import PasswordHasher

ph = PasswordHasher()
# hashed_password = ""

def create():
    if not os.path.exists("bungle.db"):
        db = connect()
        cur = db.cursor()
        cur.execute("CREATE TABLE users (username, password)")
        cur.execute("CREATE TABLE history (username, query, time_issued)")
        db.commit()

def connect():
    return mdb.connect("bungle.db")

def createUser(username, password):
    db_rw = connect()
    cur = db_rw.cursor()
    hashed_password = ph.hash(password)
    cur.execute("INSERT INTO users (username, password) VALUES(?, ?)", (username, hashed_password))
    db_rw.commit()

def validateUser(username, password):
    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("SELECT * FROM users WHERE username='{}'".format(username))
    # SQL Prevention
    try:
        stored_hash = cur.fetchall()[0][1]
    except:
        return False
        
    # Verify Password
    try:
        ph.verify(stored_hash, password)
        return True
    except:
        return False

def fetchUser(username):
    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("SELECT username FROM users WHERE username=?" , (username,))
    users = cur.fetchall()
    if len(users) < 1:
        return None
    return FormsDict(username=users[0][0])

def addHistory(username, query):
    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("INSERT INTO history (username, query, time_issued) VALUES(?, ?, ?)", (username, query, time.time()))
    db_rw.commit()

def getHistory(username):
    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("SELECT query FROM history WHERE username = ? ORDER BY time_issued DESC LIMIT 15", (username,))
    rows = cur.fetchall()
    return [row[0] for row in rows]

def clearHistory(username):
    db_rw = connect()
    cur = db_rw.cursor()
    cur.execute("DELETE from history WHERE username = ?", (username,))
    db_rw.commit()
