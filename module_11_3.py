import inspect


def introspection_info(obj):
    """Функция для интроспекции объекта."""

    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    obj_module = getattr(obj, '__module__', None)
    additional_info = {}
    if inspect.isclass(obj):
        additional_info['bases'] = [base.__name__ for base in obj.__bases__]

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        **additional_info
    }

    return info

class MyClass:
    """Пример класса для интроспекции."""

    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2

my_object = MyClass(10)
object_info = introspection_info(my_object)
print(object_info)
number_info = introspection_info(42)
print(number_info)

