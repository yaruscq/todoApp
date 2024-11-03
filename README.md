# README.md
Flask MongoDB Todo App
https://www.youtube.com/watch?v=tJxMPvzkCyo&list=PLU7aW4OZeUzwN0TsZLZUuzhc0f7OVVBcT&index=1



1. Simple Hello World app
2. Setup database connection Sign Up For mongoDB cloud
3. Setup init.py file (project configurations)
4. Setup base template
5. Setup view_todos.html file
6. Create Flask forms
7. Create insert
8. Implement Sweet alerts
9. Create retrieve
10. Implement delete
11. Implement update functinality
12. Setup .gitignore file

=================================
3.1
>>> import secrets
>>> secrets.token_hex(20)
'769999a2e3322xxxxxxxxxxxxxxxx'

=================================
After intall Flask-PyMongo, you may need to upgrade:
pip install --upgrade flask_pymongo pymongo

===========================
db.todos_flask.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "data_completed": datetime.now(timezone.utc)

        })

