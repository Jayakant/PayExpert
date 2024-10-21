import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.Implementations import EmployeeService,PayRollService,TaxService,FinancialRecordService

import pyodbc
from util.DBPropertyUtil import *
from util.DBConUtil import *

class ReportGenerator:
    def showEmployee(self,empTup):
        if(empTup == None):
            print("\nNo data")
            return
        print(f"\nId: {empTup[0]}, Name: {empTup[1]} {empTup[2]}, DOB: {empTup[3]}, Gender: {empTup[4]}, Email: {empTup[5]}, Mobile: {empTup[6]}, Address: {empTup[7]}, Position: {empTup[8]}, Joining Date: {empTup[9]}, Termination Date: {empTup[10]}")
    def showEmployees(self, empList):
        if(empList is None or len(empList) == 0):
            print("\nNo data")
            return
        for empTup in empList:
            self.showEmployee(empTup)
    def showPayRoll(self,tup):
        if(tup == None):
            print("\nNo data")
            return
        print(f"\nId: {tup[0]}, Emp Id: {tup[1]}, Start date: {tup[2]}, End date: {tup[3]}, Basic Salary: {tup[4]}, OverTimePay: {tup[5]}, Deductions: {tup[6]}, Net Salary; {tup[7]}")
    def showPayRolls(self,payRollList):
        if(payRollList is None or len(payRollList) == 0):
            print("\nNo data")
            return
        for tup in payRollList:
            self.showPayRoll(tup)
    def showTax(self,tup):
        if(tup == None):
            print("\nNo data")
            return
        print(f"\nTax Id {tup[0]}, Emp Id: {tup[1]}, Tax Year: {tup[2]}, Taxable Income: {tup[3]}, Tax amount: {tup[4]}")
    def showTaxes(self,taxList):
        if(taxList is None or len(taxList) == 0):
            print("\nNo data")
            return
        for tup in taxList:
            self.showTax(tup)
    def showFinancialRecord(self,tup):
        if(tup == None):
            print("\nNo data")
            return
        print(f"\nRecord Id: {tup[0]}, Emp Id: {tup[1]}, Record Date: {tup[2]}, Description: {tup[3]}, Amount: {tup[4]}, Record Type: {tup[5]}")
    def showFinancialRecords(self,finList):
        if(finList is None or len(finList) == 0):
            print("\nNo data")
            return
        for tup in finList:
            self.showFinancialRecord(tup)

class Main:
    @staticmethod
    def menu():
        connStr = DBPropertyUtil.getConnectionStr()
        conn = DBConUtil.getConnObj(connStr)
        # conn = pyodbc.connect(
        # "Driver={ODBC Driver 17 for SQL Server};"
        # "Server=hpVic\\SQLEXPRESS;"
        # "Database={payExpert};"
        # "Trusted_Connection=yes;"
        # )
        cursor = conn.cursor()
        
        employeeServiceObj = EmployeeService()
        payRollServiceObj = PayRollService()
        taxServiceObj = TaxService()
        financialRecordServiceObj = FinancialRecordService()
        reportGeneratorObj = ReportGenerator() 
        while(True):
            print("\n1. to access Employee data ")
            print("2. to access Payroll ")
            print("3. to access Taxes ")
            print("4. to access financial records ")
            print("0. to exit ")
            choice = int(input("Enter "))
            if(choice == 0):
                break
            elif(choice == 1):
               while(True):
                    print("\n1. to get employee by id ")
                    print("2. to get all employees ")
                    print("3. to add employee ")
                    print("4. to update an employee detail")
                    print("5 to remove employee ")
                    print("0. to go back ")
                    
                    actionChoice = int(input("Enter "))
                    
                    if(actionChoice == 0):
                        break
                    elif(actionChoice == 1):
                        empId = int(input("Enter empId "))
                        empTup = employeeServiceObj.getEmployeeById(conn,empId)
                        reportGeneratorObj.showEmployee(empTup)
                    elif(actionChoice == 2):
                        empList = employeeServiceObj.getAllEmployees(conn)
                        reportGeneratorObj.showEmployees(empList)
                    elif(actionChoice == 3):
                        employeeServiceObj.addEmployee(conn)
                    elif(actionChoice == 4):
                        id = int(input("Enter empID "))
                        employeeServiceObj.updateEmployee(conn,id)
                    elif(actionChoice == 5):
                        id = int(input("Enter empID "))
                        employeeServiceObj.removeEmployee(conn,id)
            elif(choice == 2):
                while(True):
                    print("\n1. to generate payroll ")
                    print("2. to get payroll by id ")
                    print("3. to get payrolls for employee ")
                    print("4. to get payrolls for a period ")
                    print("0. to go back ")
                    actionChoice = int(input("Enter "))

                    if(actionChoice == 0):
                        break
                    elif(actionChoice == 1):
                        payRollServiceObj.generatePayRoll(conn)
                    elif(actionChoice == 2):
                        id = int(input("\nEnter payRollId "))
                        tup = payRollServiceObj.getPayrollById(conn,id)
                        reportGeneratorObj.showPayRoll(tup)
                    elif(actionChoice == 3):
                        empId = int(input("\nEnter empId "))
                        payRollList = payRollServiceObj.getPayRollsForEmployee(conn,empId)
                        reportGeneratorObj.showPayRolls(payRollList)
                    elif(actionChoice == 4):
                        startDate = input("Enter startdate ")
                        endDate = input("Enter end date ")
                        payRollList = payRollServiceObj.getPayRollsForPeriod(conn,startDate,endDate)
                        reportGeneratorObj.showPayRolls(payRollList)
            elif(choice == 3):
                while(True):
                    print("\n1. to add tax for employee ")
                    print("2. to get tax by Id ")
                    print("3. to get tax for employee ")
                    print("4. to get tax for year ")
                    print("0. to go back ")
                    actionChoice = int(input("Enter "))
                    if(actionChoice == 0):
                        break
                    elif(actionChoice == 1):
                        taxServiceObj.calculateTax(conn)
                    elif(actionChoice == 2):
                        taxid = int(input("Enter tax id "))
                        reportGeneratorObj.showTax(taxServiceObj.getTaxById(conn,taxid))
                    elif(actionChoice == 3):
                        empId = int(input("Enter empId "))
                        reportGeneratorObj.showTaxes(taxServiceObj.getTaxesForEmployee(conn,empId))
                    elif(actionChoice == 4):
                        year = int(input("Enter year "))
                        reportGeneratorObj.showTaxes(taxServiceObj.getTaxesForYear(conn,year))
            elif(choice == 4):
                while(True):
                    print("\n1. to add financial record ")
                    print("2. to get financial record by id ")
                    print("3. to get financial record for employee ")
                    print("4. to get financial record for date ")
                    print("0. to go back ")
                    actionChoice = int(input("Enter "))
                    if(actionChoice == 0):
                        break
                    elif(actionChoice == 1):
                        financialRecordServiceObj.addFinancialRecord(conn)
                    elif(actionChoice == 2):
                        id = int(input("Enter record id "))
                        reportGeneratorObj.showFinancialRecord(financialRecordServiceObj.getFinancialRecordById(conn,id))
                    elif(actionChoice == 3):
                        empId = int(input("Enter emp id "))
                        reportGeneratorObj.showFinancialRecords(financialRecordServiceObj.getFinancialRecordsForEmployee(conn,empId))
                    elif(actionChoice == 4):
                        date = int(input("Enter year "))
                        reportGeneratorObj.showFinancialRecords(financialRecordServiceObj.getFinancialRecordsForDate(conn,date))
            
        
Main.menu()