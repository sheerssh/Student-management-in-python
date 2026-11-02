
from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul", "course": "Cloud Computing"},
    {"id": 2, "name": "Amit", "course": "DevOps"}
]

@app.route("/")
def home():
    return jsonify({
        "message": "Student Management API",
        "status": "Running"
    })


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):

    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    if not data or not data.get("name") or not data.get("course"):
        return jsonify({"error": "Name and course required"}), 400

    student = {
        "id": max([s["id"] for s in students], default=0) + 1,
        "name": data["name"],
        "course": data["course"]
    }

    students.append(student)

    return jsonify(student), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

