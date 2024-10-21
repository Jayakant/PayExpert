class FinancialRecord():
    def __init__(self,recordId, employeeId, recordDate, description, amount, recordType):
        self.recordId = recordId
        self.employeeId = employeeId
        self.recordDate = recordDate
        self.description = description
        self.amount = amount
        self.recordType = recordType