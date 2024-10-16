# 11)Write a Python function merge_dicts(dict1, dict2) that merges two dictionaries. Test it with {'a': 1} and {'b': 2}.

def merge_dicts(dict1, dict2):
    
    merge={**dict1,**dict2}
    
    print(merge)


merge_dicts({'a':1},{'b':2})