from timeit import default_timer as timer
from functools import wraps
from django.shortcuts import render

def with_timer(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        start = timer()
        response = view_func(request, *args, **kwargs)
        end = timer()

        if isinstance(response, tuple) and len(response) == 3:
            req, template, context = response
            context['time_running'] = round(end - start, 5)
            return render(req, template, context)

        return response
    return wrapper