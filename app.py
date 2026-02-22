from flask import Flask, render_template, request, jsonify
import json
import time
from logic.engine import ClarityEngine

app = Flask(__name__)
engine = ClarityEngine()

# In-memory store for scheduled tasks
scheduled_tasks = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    goals = data.get('goals', [])
    available_time = float(data.get('time', 0)) # In minutes
    
    # Process goals to find the next action
    next_action = engine.get_next_action(goals, available_time)
    
    return jsonify(next_action)

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'POST':
        data = request.json
        date = data.get('date')
        task_text = data.get('task')
        if not date or not task_text:
            return jsonify({"error": "Missing date or task"}), 400
        
        if date not in scheduled_tasks:
            scheduled_tasks[date] = []
        
        # Store as object with id and status
        new_task = {
            "id": int(time.time() * 1000),
            "text": task_text,
            "completed": False
        }
        scheduled_tasks[date].append(new_task)
        return jsonify({"success": True, "task": new_task})
    
    return jsonify(scheduled_tasks)

@app.route('/tasks/toggle', methods=['POST'])
def toggle_task():
    data = request.json
    date = data.get('date')
    task_id = data.get('taskId')
    
    if date in scheduled_tasks:
        for task in scheduled_tasks[date]:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                return jsonify({"success": True, "completed": task['completed']})
                
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5002))
    app.run(debug=True, port=port, host='0.0.0.0')
