from flask import render_template
from . import public


@public.route('/sitio/<string:page>/')
def pages(page):
    return render_template('public/{}.html'.format(page))