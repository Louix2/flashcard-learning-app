from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lernen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Datenbank-Modelle
class Ordner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('ordner.id'), nullable=True)
    unterordner = db.relationship('Ordner', backref=db.backref('parent', remote_side=[id]), cascade="all, delete")
    karten = db.relationship('Karte', backref='ordner', lazy=True, cascade="all, delete")

class Karte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frage = db.Column(db.Text, nullable=False)
    antwort = db.Column(db.Text, nullable=False)
    ordner_id = db.Column(db.Integer, db.ForeignKey('ordner.id'), nullable=False)
    wiederholen_ab = db.Column(db.DateTime, default=datetime.utcnow)

def hole_alle_karten_rekursiv(ordner):
    karten = list(ordner.karten)
    for sub in ordner.unterordner:
        karten.extend(hole_alle_karten_rekursiv(sub))
    return karten

@app.route('/')
def index():
    hauptordner = Ordner.query.filter_by(parent_id=None).all()
    edit_id = request.args.get('edit_id', type=int)
    return render_template('index.html', ordner_liste=hauptordner, aktueller_ordner=None, edit_id=edit_id)

@app.route('/ordner/<int:ordner_id>')
def ordner_ansicht(ordner_id):
    ordner = Ordner.query.get_or_404(ordner_id)
    edit_karte_id = request.args.get('edit_karte_id', type=int)
    return render_template('index.html', ordner_liste=[], aktueller_ordner=ordner, edit_karte_id=edit_karte_id)

@app.route('/erstellen', methods=['POST'])
def erstellen():
    name = request.form.get('name')
    parent_id = request.form.get('parent_id')
    pid = int(parent_id) if parent_id and parent_id != 'None' else None
    neuer = Ordner(name=name, parent_id=pid)
    db.session.add(neuer)
    db.session.commit()
    return redirect(request.referrer or url_for('index'))

@app.route('/bearbeiten/<string:typ>/<int:id>', methods=['POST'])
def bearbeiten(typ, id):
    if typ == 'ordner':
        obj = Ordner.query.get_or_404(id)
        obj.name = request.form.get('neuer_name')
        db.session.commit()
        return redirect(url_for('index'))
    else:
        obj = Karte.query.get_or_404(id)
        obj.frage = request.form.get('neue_frage')
        obj.antwort = request.form.get('neue_antwort')
        db.session.commit()
        return redirect(url_for('ordner_ansicht', ordner_id=obj.ordner_id))

@app.route('/loeschen/<string:typ>/<int:id>')
def loeschen(typ, id):
    target = Ordner.query.get_or_404(id) if typ == 'ordner' else Karte.query.get_or_404(id)
    db.session.delete(target)
    db.session.commit()
    return redirect(request.referrer or url_for('index'))

@app.route('/karte_erstellen', methods=['POST'])
def karte_erstellen():
    frage = request.form.get('frage')
    antwort = request.form.get('antwort')
    ordner_id = request.form.get('ordner_id')
    if frage and antwort:
        neue_karte = Karte(frage=frage, antwort=antwort, ordner_id=ordner_id)
        db.session.add(neue_karte)
        db.session.commit()
    return redirect(url_for('ordner_ansicht', ordner_id=ordner_id))

@app.route('/karte_gewusst/<int:karte_id>')
def karte_gewusst(karte_id):
    karte = Karte.query.get_or_404(karte_id)
    karte.wiederholen_ab = datetime.utcnow() + timedelta(days=2)
    db.session.commit()
    return "OK"

@app.route('/lernen/<int:ordner_id>')
def lernen(ordner_id):
    ordner = Ordner.query.get_or_404(ordner_id)
    jetzt = datetime.utcnow()
    alle_karten = hole_alle_karten_rekursiv(ordner)
    fällige = [k for k in alle_karten if k.wiederholen_ab <= jetzt]
    karten_daten = [{"id": k.id, "frage": k.frage, "antwort": k.antwort} for k in fällige]
    random.shuffle(karten_daten)
    return render_template('lernen.html', karten=karten_daten, ordner=ordner)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False)