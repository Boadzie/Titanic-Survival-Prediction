from flask_frozen import Freezer
import json
from main import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()