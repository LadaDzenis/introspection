import inspect
from pprint import pprint


def introspection_info(obj):
    dict_ = {}
    methods_obj = [method for method in dir(obj) if callable(getattr(obj, method))]
    attributes_obj = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    module_obj = inspect.getmodule(obj)
    dict_['type'] = type(obj).__name__
    dict_['attributes'] = attributes_obj
    dict_['methods'] = methods_obj
    dict_['module'] = module_obj
    return dict_


number_info = introspection_info(42)
pprint(number_info)



