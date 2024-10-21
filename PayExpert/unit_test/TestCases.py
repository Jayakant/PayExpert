import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from dao.Implementations import PayRollService,TaxService,FinancialRecordService,EmployeeService
from entity.PayRoll import *
from entity.Employee import *
from entity.Tax import *
from entity.FinancialRecord import *
from exception.EmployeeExceptions import EmployeeNotFound


class Test(unittest.TestCase):

    def test_calculate_gross_salary(self):
        payRollServiceObj = PayRollService()
        payRollObj = PayRoll(1,1,"2024-01-01","2064-01-01",30000.00,10000.00,1000.00,39000.00)
        grossSalary = payRollServiceObj.getGrossSal(payRollObj)
        expected_gross_salary = 40000.00
        self.assertEqual(grossSalary, expected_gross_salary)
    
    def test_calculate_net_salary(self):
        payroll_service = PayRollService()
        payRollObj = PayRoll(1,1,"2024-01-01","2064-01-01",30000.00,10000.00,1000.00,39000.00)
        net_salary = payroll_service.getNetSal(payRollObj)
        expected_net_salary = 39000.00  
        self.assertEqual(net_salary, expected_net_salary)
        
    def test_high_income_tax_calculation(self):
        tax_service = TaxService()
        tax = tax_service.getTax(100000.00)
        expected_tax = 30000  # Assuming a 30% tax rate
        self.assertEqual(tax, expected_tax)

    def test_process_payroll_for_multiple_employees(self):
        payroll_service = PayRollService()
        employee_ids = [1, 2, 3]
        for employee_id in employee_ids:
            payroll_service.generatePayRollForEmployee(employee_id)
        self.assertTrue(True)

    def test_invalid_employee_data(self):
        employee_service = EmployeeService()
        invalid_employee_id = -1
        with self.assertRaises(EmployeeNotFound):
            employee_service.getEmpById(-1)

if __name__ == '__main__':
    unittest.main()
