import os
from db import get_db
from 

def init():
    """
    Read all the JSON device and store information in the database.
    """

    files = os.listdir("Devices")
    db = get_db()
    cusor = db.cursor()

    # Get all the device already in the database
    devices = cusor.execute("SELECT * FROM devices").fetchall()
    
    for file in files:
        if file.endswith(".json"):

            with open(os.path.join("Devices", file), "r") as f:
