## What is MiddleWare?

-   Middleware is a python class that hooks into Django's request/response cycle
-   It is processed upon every request/response django handles
-   These classed can be anywhere in our django project
-   we need to register these class in settings.py MIDDLEWARE_CLASSES

## Writing you own middleware

-   A middleware is a callable that takes a request and returns a response, just like a view.
-   Middleware as a fucntion:

```python
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
```

-   Middleware as a Class:

```python
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
```

-   The get_response callable provided by Django might be the actual view (if this is the last listed middleware) or it might be the next middleware in the chain. The current middleware doesn’t need to know or care what exactly it is, just that it represents whatever comes next.
-   Middleware can either support only synchronous Python (the default), only asynchronous Python, or both.
