from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {'id': 1, 'title': 'Archana Daily Tasks', 'description': 'Wake up at 7AM', 'done': False},
    {'id': 2, 'title': 'Archana Academic Tasks', 'description': 'Finish Assignments', 'done': False},
    # Add more tasks as needed
]


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = {
            'id': len(tasks) + 1,
            'title': request.form['title'],
            'description': request.form['description']
        }
        tasks.append(new_task)
        return redirect(url_for('index'))
    return render_template('add_task.html')


@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))
    return render_template('edit_task.html', task=task)


@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
