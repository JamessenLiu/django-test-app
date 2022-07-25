import time

from apps.tasks.task import app
from apps.modules.companies.generator import export_all_companies


@app.task(priority=10)
def add(a):
    print("a", a)
    time.sleep(5)
    print("test async task")
    return


@app.task
def schedule_test():
    print("test")
    return


@app.task
def export_companies():
    export_all_companies()
    return

