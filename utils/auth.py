from django.shortcuts import render


def access_group(group, template_error='base/access_error.html'):
    def decorator(wrapped_function):
        def wrapper(self, request, *args, **kwargs):
            if not request.user.groups.filter(name=group).exists():
                return render(
                    request, template_error, {'access_group': group})
            return wrapped_function(self, request, *args, *kwargs)
        return wrapper
    return decorator
