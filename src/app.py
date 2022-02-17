from flask import Flask
from config.epsagon_config import initiate_epsagon
from controllers.invocation_blueprint import invocation_blueprint

# Epsagon
initiate_epsagon()

# Flask
app = Flask(__name__)
app.register_blueprint(invocation_blueprint, url_prefix='/invocation')








    