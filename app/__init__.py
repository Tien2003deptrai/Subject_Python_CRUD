from flask import Flask
import flask_cors  
from app.config.database import initialize_db
from app.routes.product_routes import product_bp

app = Flask(__name__)

# Initialize database
initialize_db(app)

flask_cors.cross_origin( 
origins = '*',  
methods = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT'],  
headers = None,  
supports_credentials = False,  
max_age = None,  
send_wildcard = True,  
always_send = True,  
automatic_options = False
)

# Register blueprints
app.register_blueprint(product_bp)
