from apps.goods import goods
from flask import render_template

@goods.route('/index')
def index():

    return render_template('index.html',msg="你好")