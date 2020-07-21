from flask import Flask
# importing flask

# in order for us to udr flask, we need to create an instance of our app

app = Flask(__name__)
# syntax to create flask instance

# these are called decorators and the below is the syntax for decorators to create a web toute
# block of code for default page
@app.route("/")

# created a method to display on home/ default page

def index():
    return "<h1>Welcome to MVC with flask</h1>" #<h1> is html code for creating headers
print(index())
#  index method will be called at the endpoint
#  index method will display on our home page

#  syntax to run our app
# is name is the main file, run the app
if __name__ == "__main__":
    app.run(debug=True)
#     debug=True is a built in functionality that means we are directed to the route every time we make changes without rerunning the app, saves a lot of time

# exercise - create a function called welcome_user
# create a decorator to link the page /user
# return "welcome to python flask app dear {user}

# this is an example of how we can use formatting to enter dynamic
@app.route("/<username>")
def welcome_user(username):
    return f"Welcome to python flask app, dear {username}"


if __name__ == "main":
    app.run(debug=True)

















