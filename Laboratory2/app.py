from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json

from sqlalchemy import Integer, String, Date, func, Sequence

from forms.event_form import EditEvent
from forms.plan_form import CreatePlan, EditPlan
from forms.user_form import EditUser
from forms.formBonus import BonusForm
from forms.CreateBonusForm import CreateBonus

app = Flask(__name__)
app.secret_key = 'key'

import plotly
import plotly.graph_objs as go

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:meizu123@localhost/Sasha'
else:
    app.debug = False
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgres://kdvqrwpolqqdxf:25c2172ddfb69bd5e5990b291e259f9f4c67608d2c79f257cd4cfb7c7a510241@ec2-107-20-167-241.compute-1.amazonaws.com:5432/d397i23882m0pu'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class ormUser(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(Integer, Sequence('users_id_seq', start=1, increment=1), primary_key=True)
    name = db.Column(String(40))
    surname = db.Column(String(40))
    birthday = db.Column(Date)
    userRelationShip = db.relationship("ormEvent", back_populates="user_Relation_Ship")


class ormEvent(db.Model):
    __tablename__ = 'event'
    event_id = db.Column(Integer, Sequence('event_id_seq', start=1, increment=1), primary_key=True)
    name = db.Column(String(40))
    user_id_fk = db.Column(Integer, db.ForeignKey('user.user_id'))
    category = db.Column(String(40))
    city = db.Column(String(40))
    dates = db.Column(Date)
    price = db.Column(Integer)
    hashtag = db.Column(String(40))
    adress = db.Column(String(40))
    user_Relation_Ship = db.relationship("ormUser", back_populates="userRelationShip")


class ormPlan(db.Model):
    __tablename__ = 'plan'
    event_id = db.Column(Integer, primary_key=True)
    newSkill = db.Column(String(40))
    description = db.Column(String(40))
    company = db.Column(String(40))
    category = db.Column(String(40))


class ormBonus(db.Model):
    __tablename__ = 'bonus'

    event_id = db.Column(Integer, primary_key=True)
    name = db.Column(String(40))
    value = db.Column(String(40))


@app.route('/')
def hello_world():
    text = ""
    return render_template('index.html', action="/")


@app.route('/dashboard')
def dashboard():
    query1 = (
        db.session.query(
            func.count(),
            ormPlan.category
        ).group_by(ormPlan.category)
    ).all()

    query = (
        db.session.query(
            func.count(ormEvent.hashtag),
            ormEvent.dates
        ).group_by(ormEvent.dates)
    ).all()

    dates, counts = zip(*query)
    bar = go.Bar(
        x=counts,
        y=dates
    )

    skills, user_count = zip(*query1)
    pie = go.Pie(
        labels=user_count,
        values=skills
    )
    print(dates, counts)
    print(skills, user_count)

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)


@app.route('/all/bonus')
def all_bonus():
    name = "bonus"
    name = "bonus"

    bonus_db = db.session.query(ormBonus).all()
    bonus = []
    for row in bonus_db:
        bonus.append({"event_id": row.event_id, "name": row.name, "value": row.value})
    return render_template('allBonus.html', name=name, bonus=bonus, action="/all/bonus")


@app.route('/all/event')
def all_event():
    name = "event"

    event_db = db.session.query(ormEvent).all()
    event = []
    for row in event_db:
        event.append(
            {"event_id": row.event_id, "name": row.name, "user_id_fk": row.user_id_fk, "category": row.category,
             "city": row.city, "dates": row.dates, "price": row.price, "hashtag": row.hashtag, "adress": row.adress})
    return render_template('all_event.html', name=name, events=event, action="/all/event")


@app.route('/all/user')
def all_user():
    name = "user"

    bonus_db = db.session.query(ormUser).all()
    user = []
    for row in bonus_db:
        user.append({"user_id": row.user_id, "name": row.name, "surname": row.surname, "birthday": row.birthday})
    return render_template('allUser.html', name=name, users=user, action="/all/user")


@app.route('/all/plan')
def all_plan():
    name = "plan of event"

    plan_db = db.session.query(ormPlan).all()
    plan = []
    for row in plan_db:
        plan.append({"event_id": row.event_id, "newSkill": row.newSkill, "description": row.description,
                     "company": row.company, "category": row.category})
    return render_template('all_plan.html', name=name, plans=plan, action="/all/plan")


@app.route('/create/bonus', methods=['GET', 'POST'])
def create_bonus():
    form = CreateBonus()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('create_bonus.html', form=form, form_name="New bonus", action="create/bonus")
        else:

            ids = db.session.query(ormBonus).all()
            check = True
            for row in ids:
                if row.event_id == form.event_id.data:
                    check = False

            new_var = ormBonus(
                event_id=form.event_id.data,
                name=form.name.data,
                value=form.value.data,

            )
            if check:
                db.session.add(new_var)
                db.session.commit()
                return redirect(url_for('all_bonus'))

    return render_template('create_bonus.html', form=form, form_name="New variable", action="create/bonus")


@app.route('/create/event', methods=['GET', 'POST'])
def create_event():
    form = EditEvent()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('event.html', form=form, form_name="New event", action="create/event")
        else:
            ids = db.session.query(ormUser).all()
            check = False
            for row in ids:
                if row.user_id == form.user_id_fk.data:
                    check = True
            if check:
                new_var = ormEvent(
                    name=form.name.data,
                    user_id_fk=form.user_id_fk.data,
                    category=form.category.data,
                    city=form.category.data,
                    dates=form.dates.data,
                    price=form.price.data,
                    hashtag=form.hashtag.data,
                    adress=form.adress.data,

                )

                db.session.add(new_var)
                db.session.commit()
                return redirect(url_for('all_event'))

    return render_template('event.html', form=form, form_name="New event", action="create/event")


@app.route('/create/plan', methods=['GET', 'POST'])
def create_plan():
    form = CreatePlan()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('create_plan.html', form=form, form_name="New plan", action="create/plan")
        else:

            ids = db.session.query(ormPlan).all()
            check = True
            for row in ids:
                if row.event_id == form.event_id.data:
                    check = False

            new_var = ormPlan(
                event_id=form.event_id.data,
                newSkill=form.newSkill.data,
                description=form.description.data,
                company=form.company.data,
                category=form.category.data

            )
            if check:
                db.session.add(new_var)
                db.session.commit()
                return redirect(url_for('all_plan'))

    return render_template('create_plan.html', form=form, form_name="New plan", action="create/plan")


@app.route('/create/user', methods=['GET', 'POST'])
def create_user():
    form = EditUser()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('user.html', form=form, form_name="New user", action="create/user")
        else:

            new_var = ormUser(
                name=form.name.data,
                surname=form.surname.data,
                birthday=form.birthday.data
            )

            db.session.add(new_var)
            db.session.commit()
            return redirect(url_for('all_user'))

    return render_template('user.html', form=form, form_name="New user", action="create/user")


@app.route('/delete/plan', methods=['GET'])
def delete_plan():
    event_id = request.args.get('event_id')

    result = db.session.query(ormPlan).filter(ormPlan.event_id == event_id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect(url_for('all_plan'))


@app.route('/delete/event', methods=['GET'])
def delete_event():
    event_id = request.args.get('event_id')

    result = db.session.query(ormEvent).filter(ormEvent.event_id == event_id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect(url_for('all_event'))


@app.route('/delete/user', methods=['GET'])
def delete_user():
    user_id = request.args.get('user_id')

    result = db.session.query(ormUser).filter(ormUser.user_id == user_id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect(url_for('all_user'))


@app.route('/delete/bonus', methods=['GET'])
def delete_bonus():
    event_id = request.args.get('event_id')

    result = db.session.query(ormBonus).filter(ormBonus.event_id == event_id).one()

    db.session.delete(result)
    db.session.commit()

    return redirect(url_for('all_bonus'))


@app.route('/edit/user', methods=['GET', 'POST'])
def edit_user():
    form = EditUser()
    user_id = request.args.get('user_id')
    if request.method == 'GET':

        bonus = db.session.query(ormUser).filter(ormUser.user_id == user_id).one()

        # fill form and send to user

        form.name.data = bonus.name
        form.surname.data = bonus.surname
        form.birthday.data = bonus.birthday

        return render_template('user.html', form=form, form_name="Edit user",
                               action="edit/user?user_id=" + user_id)


    else:

        if form.validate() == False:
            return render_template('user.html', form=form, form_name="Edit user", action="edit/user")
        else:

            # find user
            var = db.session.query(ormUser).filter(ormUser.user_id == user_id).one()
            print(var)

            # update fields from form data

            var.name = form.name.data
            var.surname = form.surname.data
            var.birthday = form.birthday.data
            db.session.commit()

            return redirect(url_for('all_user'))


@app.route('/edit/bonus', methods=['GET', 'POST'])
def edit_bonus():
    form = BonusForm()
    event_id = request.args.get('event_id')
    if request.method == 'GET':

        bonus = db.session.query(ormBonus).filter(ormBonus.event_id == event_id).one()

        # fill form and send to user

        form.name.data = bonus.name
        form.value.data = bonus.value

        return render_template('bonus.html', form=form, form_name="Edit variable",
                               action="edit/bonus?event_id=" + event_id)
    else:

        if form.validate() == False:
            return render_template('bonus.html', form=form, form_name="Edit variable", action="edit/bonus")
        else:

            # find user
            var = db.session.query(ormBonus).filter(ormBonus.event_id == event_id).one()
            print(var)

            # update fields from form data

            var.name = form.name.data
            var.value = form.value.data

            db.session.commit()

            return redirect(url_for('all_bonus'))


@app.route('/edit/event', methods=['GET', 'POST'])
def edit_event():
    form = EditEvent()
    event_id = request.args.get('event_id')
    if request.method == 'GET':

        bonus = db.session.query(ormEvent).filter(ormEvent.event_id == event_id).one()

        # fill form and send to user

        form.name.data = bonus.name
        form.user_id_fk.data = bonus.user_id_fk
        form.category.data = bonus.category
        form.city.data = bonus.city
        form.dates.data = bonus.dates
        form.price.data = bonus.price
        form.hashtag.data = bonus.hashtag
        form.adress.data = bonus.adress

        return render_template('event.html', form=form, form_name="Edit variable",
                               action="edit/event?event_id=" + event_id)
    else:

        if form.validate() == False:
            return render_template('event.html', form=form, form_name="Edit variable", action="edit/event")
        else:

            # find user
            var = db.session.query(ormEvent).filter(ormEvent.event_id == event_id).one()
            print(var)

            # update fields from form data

            var.name = form.name.data
            var.user_id_fk = form.user_id_fk.data

            var.category = form.category.data
            var.city = form.city.data
            var.dates = form.dates.data
            var.price = form.price.data
            var.hashtag = form.hashtag.data
            var.adress = form.adress.data

            db.session.commit()

            return redirect(url_for('all_event'))


@app.route('/edit/plan', methods=['GET', 'POST'])
def edit_plan():
    form = EditPlan()
    event_id = request.args.get('event_id')
    if request.method == 'GET':

        plan = db.session.query(ormPlan).filter(ormPlan.event_id == event_id).one()

        # fill form and send to user

        form.newSkill.data = plan.newSkill
        form.description.data = plan.description
        form.company.data = plan.company
        form.category.data = plan.category

        return render_template('edit_plan.html', form=form, form_name="Edit plan",
                               action="edit/plan?event_id=" + event_id)


    else:

        if form.validate() == False:
            return render_template('edit_plan.html', form=form, form_name="Edit plan", action="edit/plan")
        else:

            # find user
            var = db.session.query(ormPlan).filter(ormPlan.event_id == event_id).one()
            print(var)

            # update fields from form data

            var.newSkill = form.newSkill.data
            var.description = form.description.data
            var.company = form.company.data
            var.category = form.category.data

            db.session.commit()

            return redirect(url_for('all_plan'))


if __name__ == '__main__':
    app.run()
