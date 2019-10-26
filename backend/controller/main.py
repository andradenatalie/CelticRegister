from flask import Blueprint, render_template, request, redirect, url_for
from backend.models.database import Celtic
from backend.models.register import RegisterForm
from backend.data.alchemy import alchemy

bp_app = Blueprint("home", __name__)


@bp_app.route("/")
@bp_app.route("/main")
def main():
    return render_template("index.html")


@bp_app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        c = Celtic()
        form.populate_obj(c)
        alchemy.session.add(c)
        alchemy.session.commit()
        return redirect(url_for("main.main"))
    return render_template("register.html", form=form)


@bp_app.route("/list")
def list():
    celtics = Celtic.query.all()
    return render_template("list.html", pessoas=celtics)


@bp_app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = RegisterForm()
    celtic = Celtic.query.filter_by(_id=id).first()

    if form.validate_on_submit():
        form.populate_obj(celtic)
        alchemy.session.commit()

    form = RegisterForm()
    form.insert_data(celtic)
    return render_template("update.html", form=form)


@bp_app.route("/celete/<int:id>")
def delete(id):
    celtic = Celtic.query.filter_by(_id=id).first()

    alchemy.session.delete(celtic)
    alchemy.session.commit()
    return redirect(url_for("main.list"))


def configure(app):
    app.register_blueprint(bp_app)
