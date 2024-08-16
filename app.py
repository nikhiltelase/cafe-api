from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.exc import IntegrityError
import random

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        cafe_dict = self.__dict__.copy()
        cafe_dict.pop('_sa_instance_state', None)
        return cafe_dict


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    if cafes:
        random_cafe = random.choice(cafes)
        return jsonify({'cafe': random_cafe.to_dict()}), 200
    else:
        return jsonify({'response': 'No cafes found'}), 404


@app.route("/all-cafe")
def get_all_cafe():
    all_data = db.session.execute(db.select(Cafe)).scalars().all()
    cafes = [cafe.to_dict() for cafe in all_data]
    if cafes:
        return jsonify({"cafes": cafes}), 200
    else:
        return jsonify({'response': 'No cafes found'}), 404


@app.route("/search")
def search():
    query_location = request.args.get("loc")
    results = db.session.execute(db.select(Cafe).filter_by(location=query_location)).scalars().all()
    cafes = [cafe.to_dict() for cafe in results]
    if cafes:
        return jsonify({"cafes": cafes}), 200
    else:
        return jsonify({"error": "No cafes found at the specified location"}), 404


@app.route("/add", methods=['POST'])
def add():
    form = request.form
    new_cafe = Cafe(
        location=form['location'],
        name=form['name'],
        coffee_price=form['coffee_price'],
        map_url=form['map_url'],
        img_url=form['img_url'],
        can_take_calls=True,
        has_toilet=True,
        has_sockets=True,
        has_wifi=True
    )
    db.session.add(new_cafe)
    try:
        db.session.commit()
        return jsonify({"response": "success"})
    except IntegrityError:
        return jsonify({"error": "this cafe already exists."})


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.form.get('coffee_price')
    if not new_price:
        return jsonify(error={'Missing field': 'coffee_price is required'}), 400

    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404


@app.route("/delete-cafe/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")

    if api_key == 'ram':
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted cafe."}), 200
        else:
            return jsonify(error={'Not Found': 'Cafe not found'}), 404
    else:
        return jsonify(error={'Invalid API Key': 'API key is invalid'}), 403


if __name__ == '__main__':
    app.run(debug=True)
