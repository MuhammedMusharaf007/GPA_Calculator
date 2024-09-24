from flask import Flask, render_template, request

app = Flask(__name__)

# Mapping of grade names to grade points
grade_points = {"A+": 10, "A": 9, "B+": 8, "B": 7, "C": 6, "D": 5, "F": 0}


def calculate_cgpa(grades, credits):
    total_points = 0
    total_credits = 0

    for grade, credit in zip(grades, credits):
        total_points += grade_points[grade] * credit
        total_credits += credit

    cgpa = total_points / total_credits
    return cgpa


@app.route("/")
def index():
    return render_template("index.html", grade_points=grade_points)


@app.route("/calculate", methods=["POST"])
def calculate():
    grades = request.form.getlist("grades")
    credits = list(map(float, request.form.getlist("credits")))
    cgpa = calculate_cgpa(grades, credits)
    return render_template("result.html", cgpa=cgpa)


if __name__ == "__main__":
    app.run(debug=True)
