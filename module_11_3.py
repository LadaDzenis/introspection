from pprint import pprint


def introspection_info(obj):
    dict_ = {}
    attributes_obj = dir(obj)
    methods_obj = [method for method in attributes_obj if callable(getattr(obj, method))]
    module_obj = obj.__class__.__module__
    dict_['type'] = type(obj)
    dict_['attributes'] = attributes_obj
    dict_['methods'] = methods_obj
    dict_['module'] = module_obj
    return dict_


number_info = introspection_info(42)
pprint(number_info)



