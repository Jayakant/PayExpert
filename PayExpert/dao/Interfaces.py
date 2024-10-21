from datetime import date,datetime
from abc import ABC,abstractmethod
import pyodbc
   
class IEmployeeService(ABC):
    @abstractmethod
    def getEmployeeById(self,conn,id):
        pass
    
    @abstractmethod
    def getAllEmployees(self,conn):
        pass
    
    @abstractmethod
    def addEmployee(self,conn):
        pass
        
    @abstractmethod    
    def updateEmployee(self,conn,id):
        pass
    
    @abstractmethod    
    def removeEmployee(self,conn,id):
        pass
   
class IPayRollService(ABC): 
    @abstractmethod
    def generatePayRoll(self,conn):
        pass
    @abstractmethod
    def getPayrollById(self,conn,id):
        pass
    @abstractmethod
    def getPayRollsForEmployee(self,conn,id):
        pass
    @abstractmethod
    def getPayRollsForPeriod(self,conn,start,end):
        pass

class ITaxService(ABC):
    @abstractmethod
    def calculateTax(self,conn): 
        pass
    @abstractmethod
    def getTaxById(self,conn,id):
        pass
    @abstractmethod
    def getTaxesForEmployee(self,conn,id):
        pass
    @abstractmethod
    def getTaxesForYear(self,conn,year):
        pass
    
class IFinancialRecordService(ABC):
    @abstractmethod
    def addFinancialRecord(self,conn):
        pass
    @abstractmethod
    def getFinancialRecordById(self,conn,id):
        pass
    @abstractmethod
    def getFinancialRecordsForEmployee(self,conn,id):
        pass
    @abstractmethod
    def getFinancialRecordsForDate(self,conn,date):
        pass
