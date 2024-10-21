class FinancialRecordNotFound(Exception):
    def __init__(self, message="\nError, FinancialRecord not found."):
        self.message = message
        super().__init__(self.message)
class FinancialRecordAlreadyExists(Exception):
    def __init__(self, message="\nError, FinancialRecord already exists."):
        self.message = message
        super().__init__(self.message)

