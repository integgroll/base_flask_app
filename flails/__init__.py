from flask import Flask
app = Flask(__name__)


app.config["SECRET_KEY"] = "AWSSECRETKEY-SECURE_THIS_LATER"
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///flails/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["UPLOAD_FOLDER"] = "./uploads"


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

def get_or_create(session, model, **kwargs):
    """
    Helper function that will search for an item from a model in the database if one exists, if not it will return an
    object from that model that contains the kwargs as object properties
    :param session: Database session that you need to provide
    :param model: this is the model that is being searched/created
    :param kwargs: arguments that are provided to fill into the object
    :return: the model object, new and unsaved or filled out from the db
    """
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance

"""
This is the section that will combine all of the controllers, models, and templates into an overall flask application so 
the application can be compiled into individual files and a more segmented application.
"""

import flails.controllers

for piece in [flails.controllers.libraries]:
    for part in piece:
        if hasattr(part,"kwargs"):
            app.register_blueprint(part.part,**part.kwargs)
        else:
            app.register_blueprint(part.part)


from flask_migrate import Migrate
migrate = Migrate(app,db)

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)


