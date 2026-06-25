tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build API", "done": False}
]
from flask import Flask, jsonify, request
app=Flask(__name__)
@app.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify(tasks)
@app.route('/tasks/<int:id>')
def get_task(id):
    for task in tasks:
        if task["id"] == id:
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404
@app.route('/tasks',methods=['POST'])
def add_task():
    n=len(tasks)
    data=request.get_json()
    id=len(tasks)+1
    title=data['title']
    done=data['done']
    tasks.append({"id": id, "title": title, "done": done})
    if n!=len(tasks):
        return jsonify({"status":"success"}),201
    return jsonify({"error": "Task not found"}),404
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return jsonify({"status":"success"}),201
    return jsonify({"error": "Task not found"}),404
if __name__=='__main__':
    app.run(debug=True)