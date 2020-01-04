from flask import render_template, redirect, url_for
from app.models import Ciudad, Oferta, CIUDAD_DEFECTO
from . import public


@public.route('/')
@public.route('/<int:ciudad>')
def index(ciudad = None):

    if ciudad is None:
        return redirect(url_for('public.index', ciudad=CIUDAD_DEFECTO))

    oferta = Oferta.find_by_ciudad(ciudad)
    return render_template('public/portada.html', oferta=oferta)


@public.route('/ciudad/<int:id>')
def ciudad(id):
    result = Ciudad.find_by_id(id)
    return result[0]


@public.route('/sitio/<string:page>/')
def pages(page):
    return render_template('public/{}.html'.format(page))