from models import Task

def test_task_completion():

    task = Task("Learn Python")

    task.complete_task()

    assert task.completed is True