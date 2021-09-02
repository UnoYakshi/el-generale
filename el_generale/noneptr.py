from el_generale.singleton import Singleton


class _Noneptr(metaclass=Singleton):
    """
    Acts just like None except for can be called (returns None)...

    Known "bug": it's still not ``None``, comparing its ID will result in ,
                 i.e., ``None is Noneptr`` will be ``False``...

    TODO: Make sure it has all of that...
    dir(None)
    ['__bool__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__']
    """
    def __init__(self, *args, **kwargs):
        ...

    def __call__(self):
        return None

    def __bool__(self):
        return False

    def __hash__(self):
        return hash(None)

    def __str__(self):
        return 'Noneptr'

    def __unicode__(self):
        return 'Noneptr'

    def __repr__(self):
        return 'Noneptr'

    def __len__(self):
        return 0

    def __eq__(self, other):
        return True if other is None or _Noneptr else False

    def __and__(self, other):
        return False

    def __or__(self, other):
        return True if other else False

    def __xor__(self, other):
        return False if other is None or other is _Noneptr else True

# First option...
Noneptr = _Noneptr()
# Noneptr.__class__ = type.__class__(None)

# Second option...
# Noneptr = None
# Noneptr.__dict__.updated({'__call__': ret_none})
# setattr(Noneptr, '__call__', lambda: None)
