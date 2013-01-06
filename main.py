from app import app, db

from models import *
from views import *
from helpers import *

if __name__ == '__main__':
    app.run(debug=True)
