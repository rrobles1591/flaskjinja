from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['story']

debug = DebugToolbarExtension(app)

@app.route("/")
def value():
    """Generate and show form to ask words."""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def story_stuff():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)