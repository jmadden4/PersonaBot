import os
from flask import Flask
app = Flask(__name__)

from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
print 'made it'
#COV = None
#if os.environ.get('FLASK_COVERAGE'):
#   import coverage
#   COV = coverage.coverage(branch=True, include='app/*')
#   COV.start()

 
if __name__ == '__main__':
    manager.run()
