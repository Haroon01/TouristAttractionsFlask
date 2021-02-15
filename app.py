from flask import Flask, render_template, request, redirect, url_for
from locations import Locations
from forms import AddLocationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_PROJECT'

form = AddLocationForm()
visit = Locations()
categories = {"recommended": "Recommended", "tovisit": "Places To Go", "visited": "Visited!!!", }

UP_ACTION = "\u2197"
DEL_ACTION = "X"

@app.route("/<category>", methods=["GET", "POST"])
def locations(category):
  locations = visit.get_list_by_category(category)
  ## Check the request for form data and process
  if request.method == "POST":
    print(request.form.items())
    [(name, action)] = request.form.items()

    if action == UP_ACTION:
      visit.moveup(name)
    elif action == DEL_ACTION:
      visit.delete(name)

  add_location_class = AddLocationForm()
  ## Return the main template with variables
  return render_template("locations.html",
  category = category,
  categories = categories,
  locations = locations,
  add_location = add_location_class)

@app.route("/add_location", methods=["POST"])
def add_location():
  ## Validate and collect the form data

  if True:
      name=None
      description=None
      category=None
      visit.add(name, description, category)

  ## Redirect to locations route function
  return ""

@app.route("/")
def index():

  ## Redirect to locations route function
  return ""