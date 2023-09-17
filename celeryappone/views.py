from django.shortcuts import render
from celeryprojectone.celery import mul
from celeryappone.tasks import add
from celery.result import AsyncResult

# def index(request):       # Enqueue task using 'delay'
#     print("Results: ")
#     res = mul.delay(7, 9)
#     print("The Result is ", res)
#     res2 = add.delay(5, 8)
#     print("The Result is ", res2)
#     return render(request, "celeryappone/home.html")


# def index(request):         # Enqueue task using 'apply_async' function 
#     print("Results: ")
#     res = mul.apply_async(args=[7, 9])
#     print("The Result is ", res)
#     res2 = add.apply_async(args=[5, 8])
#     print("The Result is ", res2)
#     return render(request, "celeryappone/home.html")

def index(request):
    res = mul.delay(7, 9)
    return render(request, "celeryappone/home.html", {'res': res})

def check_res(request, task_id):
    res = AsyncResult(task_id)    # Using the task_id i'm fetching the result
    print("Ready: ", res.ready())
    print("Successful: ", res.successful())
    print("Failed: ", res.failed())
    return render(request, "celeryappone/result.html", {'res': res})

def product(request):
    return render(request, "celeryappone/product.html")

def about(request):
    return render(request, "celeryappone/about.html")

def contact(request):
    return render(request, "celeryappone/contact.html")