from dao.Interfaces import *
from entity.Employee import *
from entity.FinancialRecord import *
from exception.EmployeeExceptions import *
from exception.PayRollExceptions import *
from exception.TaxExceptions import *
from exception.FinancialRecordExceptions import *

class EmployeeService(IEmployeeService):
    def getEmployeeById(self,conn,empId):
        try:
            cursor = conn.cursor()

            # empId = int(input("Enter empId "))
            data = cursor.execute(f"select * from Employee where EmployeeId = {empId}").fetchone()
            if(data is None or empId<0):
                raise EmployeeNotFound
            return data
        except Exception as e:
            print(e)
            raise e

    def getAllEmployees(self,conn):
        cursor = conn.cursor()
        data = cursor.execute("select * from Employee").fetchall()
        return list(data)
    
    def addEmployee(self,conn):
        try:
            cursor = conn.cursor()
            empId = int(input("\nEnter id "))
            data = cursor.execute(f"select * from Employee where EmployeeId = {empId}").fetchone()
            if(data != None):
                raise EmployeeAlreadyExists
            firstName = input("Enter firstName ")
            lastName = input("Enter lastName ")
            dob = input("Enter dob ")
            gender = input("Enter gender ")
            email = input("Enter email ")
            phoneNumber = input("Enter phone number ")
            address = input("Enter address ")
            position = input("Enter position ")
            joiningDate = input("Enter joining date ")
            terminationDate = input("Enter termination date ")
            newEmp = Employee(empId,firstName,lastName,dob,gender,email,phoneNumber,address,position,joiningDate,terminationDate)
            
            cursor.execute("insert into Employee values(?,?,?,?,?,?,?,?,?,?,?)",(newEmp.employeeId,newEmp.firstName,newEmp.lastName,newEmp.dateOfBirth,newEmp.gender,newEmp.email,newEmp.phoneNumber,newEmp.address,newEmp.position,newEmp.joinigDate,newEmp.terminationDate))
            conn.commit()
            print(f"\nAdded {newEmp.firstName} {newEmp.lastName} successfully! \n")
        except Exception as e:
            print(e)
        
    def updateEmployee(self,conn,id):
        try:
            cursor = conn.cursor()
            # id = int(input("Enter empID "))
            data = cursor.execute(f"select * from Employee where EmployeeId = {id}").fetchone()
            if(data is None):
                raise EmployeeNotFound
            # data = cursor.execute(f"select * from Employee where EmployeeId = {id}").fetchone()
            
            firstName = input("Enter firstName ")
            lastName = input("Enter lastName ")
            dob = input("Enter dob ")
            gender = input("Enter gender ")
            email = input("Enter email ")
            phoneNumber = input("Enter phone number ")
            address = input("Enter address ")
            position = input("Enter position ")
            joiningDate = input("Enter joining date ")
            terminationDate = input("Enter termination date ")
            # print("fN ",firstName)
            firstName = firstName if firstName!="" else data.FirstName
            lastName = lastName if lastName!="" else data.LastName
            dob = dob if dob!="" else data.DateOfBirth
            gender = gender if gender!="" else data.Gender
            email = email if email!="" else data.Email
            phoneNumber = phoneNumber if phoneNumber!="" else data.PhoneNumber
            address = address if address!="" else data.Address
            position = position if position!="" else data.Position
            joiningDate = joiningDate if joiningDate!="" else data.JoiningDate
            terminationDate = terminationDate if terminationDate!="" else data.TerminationDate

            cursor.execute("update Employee set FirstName=?,LastName=?,DateOfBirth=?,Gender=?,Email=?,PhoneNumber=?,Address=?,Position=?,JoiningDate=?,TerminationDate=? where EmployeeId=?",(firstName,lastName,dob,gender,email,phoneNumber,address,position,joiningDate,terminationDate,id))
            conn.commit()
            print(f"\nUpdated {data[1]} {data[2]} details successflly!\n")
        except Exception as e:
            print(e)
        
    def removeEmployee(self,conn,id):
        try:
            cursor = conn.cursor()
            # id = int(input("Enter empID "))
            data = cursor.execute(f"select * from Employee where EmployeeId = {id}").fetchone()
            if(data is None):
                raise EmployeeNotFound
            toRemoveEmployee = cursor.execute("select * from Employee where EmployeeId=?",(id)).fetchone()
            # removing data from others tables to resolve foreign key conflict
            cursor.execute("delete from PayRoll where EmployeeId=?",(id))
            cursor.execute("delete from Tax where EmployeeId=?",(id))
            cursor.execute("delete from FinancialRecord where EmployeeId=?",(id))
            
            cursor.execute("delete from Employee where EmployeeId=?", (id))
            print(f"Removed {toRemoveEmployee[1]} {toRemoveEmployee[2]} successfully!\n ")
            conn.commit()
        except Exception as e:
            print(e)
            
    def getEmpById(self,id):
        try:
            if(id<0):
                raise EmployeeNotFound
            else:
                pass
                # return Employee(id)
        except Exception as e:
            print(e)
            raise e
        
class PayRollService(IPayRollService):
    
    def getBasicSal(self,position):
        if(position == "Trainee"):
            return 40000.00
        if(position == "Manager"):
            return 120000.00
    def getOverTimePay(self,position):
        if(position == "Trainee"):
            return 2000.00
        if(position == "Manager"):
            return 6000.00
    def getDeductions(self,position):
        if(position == "Trainee"):
            return 2000.00
        if(position == "Manager"):
            return 6000.00
        
    def getGrossSal(self,payRollObj):
        return payRollObj.basicSalary+payRollObj.overTimePay
    
    def getNetSal(self,payRollObj):
        return payRollObj.basicSalary+payRollObj.overTimePay - payRollObj.deductions
        
    def generatePayRoll(self,conn):
        try:
            cursor = conn.cursor()
            payRollId = int(input("\nEnter payRollId "))
            data = cursor.execute("select * from PayRoll where PayRollId=?",(payRollId)).fetchone()
            if(data != None):
                raise PayRollAlreadyExists
            empId = int(input("\nEnter empId to generate payRoll "))
            empData = cursor.execute("select * from Employee where EmployeeId=?",(empId)).fetchone()
            # basicSal = self.getBasicSal(empData[8])
            # overTimePay = self.getOverTimePay(empData[8])
            # deductions = self.getDeductions(empData[8])
            basicSal = round(float(input("Enter basic salary ")),2)
            overTimePay = round(float(input("Enter over time pay ")),2)
            deductions = round(float(input("Enter deductions ")),2)

            # cursor.execute("insert into PayRoll values(?, ?, ?, ?, ?, ?, ?, ?)",(payRollId,employeeId,payPeriodStartDate,payPeriodEndDate,basicSalary,overTimePay,deductions,netSalary))
            cursor.execute("insert into PayRoll values(?, ?, ?, ?, ?, ?, ?, ?)",(payRollId,empData[0],empData[9],empData[10], basicSal,overTimePay,deductions,basicSal+overTimePay-deductions))

            conn.commit()
            print("\nGenerated PayRoll successfully !\n")
        except Exception as e:
            print(e)
            
    def getPayrollById(self,conn,id):
        try:
            # id = int(input("\nEnter payRollId "))
            cursor = conn.cursor()
            data = cursor.execute(f"select * from PayRoll where PayRollId = {id}").fetchone()
            if(data is None):
                raise PayRollNotFound
            return data
        except Exception as e:
            print(e)
            
    def getPayRollsForEmployee(self,conn,empId):
        cursor = conn.cursor()
        try:
            # empId = int(input("\nEnter empId "))
            empData = cursor.execute("select * from Employee where EmployeeId=?",(empId)).fetchone()
            if(empData is None):
                raise EmployeeNotFound
            data = cursor.execute(f"select * from PayRoll where EmployeeId = {empId}").fetchall()
            return list(data)
        except Exception as e:
            print(e)
            
    def getPayRollsForPeriod(self,conn,startDate,endDate):
        # startDate = input("Enter startdate ")
        # endDate = input("Enter end date ")
        cursor = conn.cursor()
        data = cursor.execute("select * from PayRoll where PayPeriodStartDate >= ? and PayPeriodEndDate <= ?",(startDate,endDate)).fetchall()
        return list(data)
    
    def generatePayRollForEmployee(self,empId):
        pass
     
class TaxService(ITaxService):
    def getTax(self,basicSal):
        return basicSal*30/100
    def calculateTax(self,conn):
        try:
            cursor = conn.cursor()
            taxId = int(input("Enter taxId "))
            data = cursor.execute(f"select * from Tax where TaxId = {taxId}").fetchone()
            if(data != None):
                raise TaxAlreadyExists
            empId = int(input("Enter empId "))
            data = cursor.execute(f"select * from Employee where EmployeeId = {empId}").fetchone()
            if(data is None):
                raise EmployeeNotFound
            taxYear = input("Enter tax year ")
            taxableSal = round(float(input("Enter taxable income ")),2)
            tax = (taxableSal/100)*30
            cursor.execute("insert into Tax values(?,?,?,?,?)",(taxId,empId,taxYear,taxableSal,tax))
            conn.commit()
            print(f"Added tax!")
        except Exception as e:
            print(e)

    def getTaxById(self,conn,taxid):
        cursor = conn.cursor()
        try:
            # taxid = int(input("Enter tax id "))
            data = cursor.execute(f"select * from Tax where TaxId={taxid}").fetchone()
            if(data is None):
                raise TaxNotFound
            return data
        except Exception as e:
            print(e)
    def getTaxesForEmployee(self,conn,empId):
        try:
            cursor = conn.cursor()
            # empId = int(input("Enter empId "))
            data = cursor.execute(f"select * from Employee where EmployeeId = {empId}").fetchone()
            if(data is None):
                raise EmployeeNotFound
            data = cursor.execute(f"select * from Tax where EmployeeId={empId}").fetchall()
            return list(data)
        except Exception as e:
            print(e)
            
    def getTaxesForYear(self,conn,year):
        cursor = conn.cursor()
        # year = int(input("Enter year "))
        data = cursor.execute("select * from Tax where year(TaxYear) = ?",(year)).fetchall()
        return data
class FinancialRecordService(IFinancialRecordService):
    def addFinancialRecord(self,conn):
        
        try:
            cursor = conn.cursor()
            recordId = int(input("Enter recordId "))
            data = cursor.execute("select * from FinancialRecord where RecordId=?",(recordId)).fetchone()
            if(data != None):
                raise FinancialRecordAlreadyExists
            employeeId = int(input("Enter empId "))
            data = cursor.execute(f"select * from Employee where EmployeeId = {employeeId}").fetchone()
            if(data is None):
                raise EmployeeNotFound
            recordDate = input("Enter date ")
            description = input("Enter description ")
            amount = round(float(input("Enter amount ")),2)
            recordType = input("Enter recordType ")
            
            obj = FinancialRecord(recordId,employeeId,recordDate,description,amount,recordType)
            # cursor.execute("insert into FinancialRecord values(?,?,?,?,?,?)",(recordId,employeeId,recordDate,description,amount,recordType))
            cursor.execute("insert into FinancialRecord values(?,?,?,?,?,?)",(obj.recordId,obj.employeeId,obj.recordDate,obj.description,obj.amount,obj.recordType))

            cursor.commit()
            print(f"\nAdded financial record with empId {obj.employeeId} successfully! ")
        except Exception as e:
            print(e)
            
    def getFinancialRecordById(self,conn,id):
        try:
            cursor = conn.cursor()
            # id = int(input("Enter record id "))
            data = cursor.execute(f"select * from FinancialRecord where RecordId={id}").fetchone()
            if(data is None):
                raise FinancialRecordNotFound
            return data
        except Exception as e:
            print(e)
            
    def getFinancialRecordsForEmployee(self,conn,empId):
        cursor = conn.cursor()
        # empId = int(input("Enter emp id "))
        data = cursor.execute(f"select * from Employee where EmployeeId = {empId}").fetchone()
        if(data is None):
            raise EmployeeNotFound
        data = cursor.execute(f"select * from FinancialRecord where EmployeeId={empId}").fetchall()
        return list(data)
    def getFinancialRecordsForDate(self,conn,date):
        cursor = conn.cursor()
        # date = int(input("Enter year "))
        data = cursor.execute("select * from FinancialRecord where year(RecordDate) = ?",(date)).fetchall()
        return list(data)