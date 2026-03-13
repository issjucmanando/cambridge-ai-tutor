from flask import Flask, render_template, request

app = Flask(__name__)

def generate_notes(subject, topic, level):

    notes = f"""
Subject: {subject}
Level: {level}
Topic: {topic}

Key Points:
- Understand main concepts
- Learn important definitions
- Study examples
- Practice Cambridge style questions
"""

    return notes


@app.route("/", methods=["GET","POST"])

def home():

    notes = ""

    if request.method == "POST":

        subject = request.form["subject"]
        topic = request.form["topic"]
        level = request.form["level"]

        notes = generate_notes(subject, topic, level)

    return render_template("index.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)