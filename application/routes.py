# routes.py
from datetime import datetime, timezone
from application import app
from flask import render_template, request, flash, redirect, url_for
from bson import ObjectId

from application.forms import TodoForm
from application import db, todos_collection



@app.route('/')
def get_todos():
    todos = []
    # -1 means descending order
    for todo in todos_collection.find().sort("date_created", -1):
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)
    return render_template('view_todos.html', title='Layout Page', todos=todos)
    # return render_template('view_todos.html', title='Layout Page')


@app.route('/add_todo', methods=['POST', 'GET'])
def add_todo():
    if request.method == 'POST':
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        todos_collection.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.now(timezone.utc)

        })
        flash("Todo succesfully added", "success")
        return redirect('/')
    else: 
        form = TodoForm()
    return render_template("add_todo.html", form = form)


@app.route('/test')
def test():
    if db is not None:
        # print(mongodb_client.db.list_collection_names())
        return "Atlas MogoDB connected"
    else:
        return "failed"
    


@app.route("/update_todo/<id>", methods = ['POST', 'GET'])
def update_todo(id):
    if request.method == 'POST':
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data

        todos_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"name": todo_name,
         "description": todo_description,
         "completed": completed,
         "date_created": datetime.now(timezone.utc)   
         }})
        
        flash("Todo successfully updated", "success")
        return redirect('/')
    
    else:
        form = TodoForm()
        todo = todos_collection.find_one_or_404({"_id": ObjectId(id)})
        print(todo)
        form.name.data = todo.get('name', None)
        form.description.data = todo.get('description', None)
        form.completed.data = todo.get('completed', None)
    
    return render_template('add_todo.html', form = form)



@app.route("/delete_todo/<id>")
def delete_todo(id):
    todos_collection.find_one_and_delete({"_id": ObjectId(id)})
    flash("Todo deleted", "success")
    return redirect('/')