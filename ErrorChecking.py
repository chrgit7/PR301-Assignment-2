class ErrorChecking:
    def __init__(self):
        self.message = []  # argument, function name, class name

    def check(self, variable, varType, message):
        message.replace(" ", "")
        self.message = message.split(",")
        errorMessage = {
            "int": lambda: self.notAInt(variable),
            "string": lambda: self.notAString(variable),
            "list": lambda: self.notAList(variable),
            "bool": lambda: self.notABool(variable),
            "float": lambda: self.notAFloat(variable),
            "floatOrInt": lambda: self.notAFloatOrInt(variable)
        }
        errorMessage[varType]()

    def notAInt(self, variable):
        if not isinstance(variable, int):
            print(self.error_message("int"))

    def notAString(self, variable):
        if not isinstance(variable, str):
            print(self.error_message("string"))

    def notAList(self, variable):
        if not isinstance(variable, list):
            print(self.error_message("list"))

    def notABool(self, variable):
        if not isinstance(variable, bool):
            print(self.error_message("list"))

    def notAFloat(self, variable):
        if not isinstance(variable, float):
            print(self.error_message("float"))

    def notAFloatOrInt(self, variable):
        if not isinstance(variable, float) and not isinstance(variable, int):
            print(self.error_message("float or int"))

    def error_message(self, reqType):
        return "The %s argument of the %s function inside the %s class is not a %s!" %\
               (self.message[0], self.message[1], self.message[2], reqType)


