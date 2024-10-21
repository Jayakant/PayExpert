class PayRoll():
    def __init__(self, payRollId, employeeId, payPeriodStartDate, payPeriodEndDate, basicSalary,
                overTimePay, deductions, netSalary):
        self.payRollId = payRollId
        self.employeeId = employeeId
        self.payPeriodStartDate = payPeriodStartDate
        self.payPeriodEndDate = payPeriodEndDate
        self.basicSalary = basicSalary
        self.overTimePay = overTimePay
        self.deductions = deductions
        self.netSalary = netSalary