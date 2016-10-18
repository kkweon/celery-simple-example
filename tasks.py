from celery import Celery

app = Celery('tasks', 
             backend='redis://localhost', 
             broker='redis://localhost')

@app.task
def add(x, y):
    print("{} + {} = {}".format(x, y, x+y))
    return x + y

@app.task
def xsum(numbers):
    return sum(numbers)
    
if __name__ == '__main__':
    
    # Basic Example
    result = add.delay(10, 10)
    print(result.get())
    result = add.apply_async((10, 10))
    print(result.get())

