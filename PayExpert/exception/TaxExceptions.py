class TaxNotFound(Exception):
    def __init__(self, message="\nError, Tax not found."):
        self.message = message
        super().__init__(self.message)
class TaxAlreadyExists(Exception):
    def __init__(self, message="\nError, Tax already exists."):
        self.message = message
        super().__init__(self.message)

