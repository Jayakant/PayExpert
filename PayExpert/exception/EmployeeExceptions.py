class EmployeeNotFound(Exception):
    def __init__(self, message="\nError, Employee not found."):
        self.message = message
        super().__init__(self.message)
class EmployeeAlreadyExists(Exception):
    def __init__(self, message="\nError, Employee already exists."):
        self.message = message
        super().__init__(self.message)

