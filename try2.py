from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to ai world</h1>"

friends = [
    {'id': 1,
     'name': "ravikiran",
     'email': "ravikiran@gmail.com"
    },  
    { 'id': 2,
    'name': "srinaveen",
    'email': "srinaveen@gmail.com"
    }
]

@app.route("/users")
def emp_details():
    return render_template("details.html", content=friends)

@app.route("/users/<int:employee_id>")
def users(employee_id):
    for employee in friends:
        if employee['id'] == employee_id:
            emp_data = {'name': employee['name'], 'email': employee['email']}
            return render_template("user.html", emp_data=emp_data)
    return 'Employee not found'

if __name__ == "__main__":
    app.run(debug=True)
