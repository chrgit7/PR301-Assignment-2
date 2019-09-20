class ErrorChecking:
    def __init__(self):
        self.message = []  # argument, function name, class name

    def check(self, variable, vartype, message):
        message.replace(" ", "")
        self.message = message.split(",")
        errormessage = {
            "int": lambda: self.not_a_int(variable),
            "string": lambda: self.not_a_string(variable),
            "list": lambda: self.not_a_list(variable),
            "bool": lambda: self.not_a_bool(variable),
            "float": lambda: self.not_a_float(variable),
            "floatOrInt": lambda: self.not_a_float_or_int(variable)
        }
        errormessage[vartype]()

    def not_a_int(self, variable):
        if not isinstance(variable, int):
            print(self.error_message("int"))

    def not_a_string(self, variable):
        if not isinstance(variable, str):
            print(self.error_message("string"))

    def not_a_list(self, variable):
        if not isinstance(variable, list):
            print(self.error_message("list"))

    def not_a_bool(self, variable):
        if not isinstance(variable, bool):
            print(self.error_message("list"))

    def not_a_float(self, variable):
        if not isinstance(variable, float):
            print(self.error_message("float"))

    def not_a_float_or_int(self, variable):
        if not isinstance(variable, float) and not isinstance(variable, int):
            print(self.error_message("float or int"))

    def error_message(self, reqtype):
        return "The %s argument of the %s function inside the %s class is not a %s!" %\
               (self.message[0], self.message[1], self.message[2], reqtype)


