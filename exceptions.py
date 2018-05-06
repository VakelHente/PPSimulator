class ProtocolItemError(Exception):
    """Single protocol item is not valid."""
    functions = {
        "inputFunction": "Input Function",
        "statesFunction" : "States Function",
        "outputFunction" : "Output Function"
        }
    def __init__(self, item, function=None):
        self.item = item
        self.function = function

    def __str__(self):
        if self.function:
            return "{}: '{}' is not valid.".format(self.functions[self.function], self.item)
        return "Item: '{}' is not valid.".format(self.item)