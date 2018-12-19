#src/app.py

from flask import Flask

from config import app_config
from models import db, bcrypt

# import user_api blueprint
from views.WorkflowView import workflow_api as workflow_blueprint
import os


def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  # initializing bcrypt and db
  bcrypt.init_app(app)
  db.init_app(app)

  app.register_blueprint(workflow_blueprint, url_prefix='/api/v1/')

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your part 2 endpoint is working'

  return app

if __name__ == '__main__':
  app = create_app("production")

  app.run(host='0.0.0.0', port=5000)