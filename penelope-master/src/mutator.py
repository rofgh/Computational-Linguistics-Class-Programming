

class Mimic(object):
    """ Wrap the object by composition and act as ducktype """
    def __init__(self, core):
        self._core = core
        self._internal_props = {}

    # Cascade to get val from dict or the core object
    def __getattr__(self, attr):
        if attr in self._internal_props:
            return self._internal_props[attr]
        return getattr(self._core, attr)

    # def __setattr__(self, prop, val):
    #     try:
    #         self.__dict__._internal_props[prop] = val
    #         object.__setattr__(self, '_internal_props', self.__dict__._internal_props)
    #     except AttributeError:
    #         self.__dict__[prop] = val
    #     return val

    # Add props and vals to the internal dict if present
    def set_prop(self, prop, val):
        self._internal_props[prop] = val
        setattr(self._core, prop, val)
        return val

    # Wrapper to get the present member props
    def _members(self):
        coredict = vars(self._core)
        return {**coredict, **self._internal_props} # the dict overrides


class Mutator:
    """ A manipulator for handling command mutation and examination of a mimic object """
    def __init__(self, target=None):
        self._mimic = Mimic(target)

    # Parse a command into its parts, and run
    def command(self, command):
        prefix, suffix, *_ = command.split(" ")
        prefix = prefix.lower()
        # TODO: Consider command pattern here
        if prefix == "get":
            if suffix == "*":
                return self.render()
            else:
                return self.get_prop(suffix)
        elif prefix == "set":
            nprop, nval = suffix.split("=")
            self.set_prop(nprop, nval)
        else:
            raise ValueError(f"Invalid command structure for command: {command}")

    # Get return the current value of a target prop
    def get_prop(self, prop):
        return getattr(self._mimic, prop)

    # Set will set the contents of a prop
    def set_prop(self, prop, val):
        self._mimic.set_prop(prop, val)
        return val

    # Print out object props and current values
    def render(self):
        return "Currently: " + str(self._mimic._members())

    def __str__(self):
        return self.render()

    def __repr__(self):
        return self.render()

    # Finalize the object mimic with new props
    def write(self):
        return self._mimic
