from flask import Flask, render_template
from apps import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return render_template('TEST.html')

from apps.goods import goods
app.register_blueprint(goods)
