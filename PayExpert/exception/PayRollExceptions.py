class PayRollAlreadyExists(Exception):
    def __init__(self, message="\nError, PayRoll already exists."):
        self.message = message
        super().__init__(self.message)
        
class PayRollNotFound(Exception):
    def __init__(self, message="\nError, PayRoll not found."):
        self.message = message
        super().__init__(self.message)
