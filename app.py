from flask import Flask, request, render_template
from stories import story2
# request.args returns a dictionary

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route("/home")
def home():
    story_parts = story2.prompts
    return render_template("home.html", story_parts=story_parts)


@app.route('/story')
def story():
    new_story = story2.generate(request.args)
    return render_template("story.html", new_story=new_story)
