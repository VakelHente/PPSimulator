
class ObjectDict(dict):
    def __getattr__(self, key):
        try:
            # Throws exception if not in prototype chain
            return object.__getattribute__(self, key)
        except AttributeError:
            try:
                return self[key]
            except KeyError:
                raise AttributeError(key)

    def __setattr__(self, key, value):
        try:
            # Throws exception if not in prototype chain
            object.__getattribute__(self, key)
        except AttributeError:
            try:
                self[key] = value
            except:
                raise AttributeError(key)
        else:
            object.__setattr__(self, key, value)

def dictToObj(cls, oDict):
    """
    Convert dictionary to class.

    @param cls   : Class
    @param oDict : Dict or ordered Dict
    @return      : Object with with all definition of class and attributes from dict
    """
    if isinstance(oDict, dict):
        return cls((k, dictToObj(cls, v)) for k, v in oDict.items())
    elif isinstance(oDict, (list, tuple)):
        return type(oDict)(dictToObj(cls, v) for v in oDict)
    else:
        return oDict