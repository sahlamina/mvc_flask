#MVC - Model View Controllers
* Not only used in python, also used in javascript, HTML CSS
* In order for us to show our work, we use a web browser
* Controller - needs to display information in view, which is the web browser. It is similar to the run file displaying info in the terminal
```` app.run()````
- syntax for runnning
- view: python and HTML displayed passed an argument at run time in the browser and displayed the info

* creating a dynamic page that accepts any name in as the username
````python @app.route("/<username>")
def welcome_user(username):
    return f"Welcome to python flask app, dear {username}"
````
* 3 amigos, persona, Information Radiators with example, scrum artefacts, scrum events, scrum roles, sprint review and sprint retrospective, Starfish retrospective, Root cause Analysis-part of retrospective, agile vales and principles. There are many more things in agile and scrum for which resources have been provided and you have done it practically like user story, epic etc. Have a solid answer ready for what is Agile?
Model
* bootstrap - lets us style our page using CSS
* we can utilise the built in functions
- bootstrapping is essentially c&ping code to use in your programme
- S showed us a website with a toolbar and explained that the toolbar was a parent class and the other pages inherited from it

- Syntax for inheritance in html:
```{% extends "base.html"%}```