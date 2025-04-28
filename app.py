from flask import Flask, render_template, request, redirect, url_for
from auth import login, register

app = Flask(__name__, template_folder="templates")
todos = [{"task": "sample todo", "done": False}]


@app.route("/")  #
def index():
    return render_template("index.html", todos=todos)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if login(username, password):
            return redirect(url_for("index"))
        else:
            return "Login failed.Invalid username or password.", 401
    return render_template("login.html")


# Register route
@app.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        
        if register(username, password): 
            return "Registration successful! Please log in." 
        else:
            return "Registration failed. User might already exist.", 400  # Handle failed registration

    return render_template("register.html")


@app.route("/add", methods=["POST"])  #
def add():
    todo = request.form['todo']
    todos.append(({"task": todo, "done": False}))
    return redirect(url_for("index"))


@app.route("/edit/<int:index>", methods=['GET', 'POST'])
def edit(index):
    print(request.method)
    todo = todos[index]
    print(index)
    if request.method == 'POST':
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@app.route("/check/<int:index>", methods=['POST'])
def check(index):
    todo = todos[index]
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    # todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
