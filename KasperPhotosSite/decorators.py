from django.http import HttpResponseRedirect, HttpResponse

def allowedGroups(groups=[]):
    def decorator(func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in groups:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse("You do not have the proper permissions")

            return func(request, *args, **kwargs)
        return wrapper_func
    return decorator