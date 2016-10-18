from celery import Celery

app = Celery('tasks', 
             backend='redis://localhost', 
             broker='redis://localhost')

@app.task
def add(x, y):
    print("{} + {} = {}".format(x, y, x+y))
    return x + y

