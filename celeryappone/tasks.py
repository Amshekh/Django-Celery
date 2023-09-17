from celery import shared_task
from time import sleep

@shared_task(name = "addition_task_test")
def add(x, y):
    sleep(15)
    return x + y