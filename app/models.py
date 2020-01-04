from app import db

CIUDAD_DEFECTO = 1

class Ciudad(db.Model):
    __tablename__ = 'ciudades'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)

    # Relations
    ofertas = db.relationship('Oferta', backref="ciudad")
    tiendas = db.relationship('Tienda', backref="tienda")

    @staticmethod
    def all():
        return Ciudad.query.all()

    @staticmethod
    def find_by_id(id):
        return Ciudad.query.get(id)


class Tienda(db.Model):
    __tablename__ = 'tiendas'

    id = db.Column(db.Integer, primary_key=True)
    ciudad_id = db.Column(db.Integer, db.ForeignKey('ciudades.id'))
    nombre = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    descripcion = db.Column(db.Text)
    direccion = db.Column(db.Text)

    # Relations
    ofertas = db.relationship('Oferta', backref="tienda")

    # Methods


class Oferta(db.Model):
    __tablename__ = 'ofertas'

    id = db.Column(db.Integer, primary_key=True)
    ciudad_id = db.Column(db.Integer, db.ForeignKey('ciudades.id'))
    tienda_id = db.Column(db.Integer, db.ForeignKey('tiendas.id'))
    nombre = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    condiciones = db.Column(db.Text)
    foto = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float)
    descuento = db.Column(db.Float)
    fec_publicacion = db.Column(db.DateTime)
    fec_expiracion = db.Column(db.DateTime)
    compras = db.Column(db.Integer)
    umbral = db.Column(db.Integer)
    revisada = db.Column(db.Boolean)

    # Relations
    # ciudad = db.relationship('Ciudades', foreign_keys=ciudad_id)
    # tienda = db.relationship('Tiendas', foreign_keys=tienda_id)

    @staticmethod
    def all():
        return Oferta.query.all()


    @staticmethod
    def find_by_ciudad(id):
        return Oferta.query.filter_by(ciudad_id=id).first()
