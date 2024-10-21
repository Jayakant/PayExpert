create database payExpert

use payExpert

create table Employee(EmployeeId int primary key,
FirstName varchar(20),
LastName varchar(20),
DateOfBirth date,
Gender varchar(20),
Email varchar(20),
PhoneNumber varchar(14),
Address varchar(50),
Position varchar(20),
JoiningDate date,
TerminationDate date)

insert into Employee values(1,
'Jay',
'Purushoth',
'2002-08-05',
'Male',
'jay@gmail.com',
'+91 8838902352',
'10, Mission st, Cud, TN',
'Trainee',
'2024-12-2',
'2064-12-2')

insert into Employee values(2,
'Monal',
'Patel',
'2002-07-27',
'Female',
'monalJay@gmail.com',
'+91 8838902353',
'10, Mission st, Cud, TN',
'Trainee',
'2024-12-2',
'2064-12-2')

insert into Employee values(3,
'Shalini',
'S',
'2003-03-21',
'Female',
'Shalz@gmail.com',
'+91 8838902354',
'10, Mission st, Cud, TN',
'Trainee',
'2024-12-2',
'2064-12-2')

insert into Employee values(4,
'Claudia',
'Doumit',
'2000-01-21',
'Female',
'vicky@gmail.com',
'+91 8838902355',
'11, Mission st, Vad, Cal',
'Team Leader',
'2022-12-2',
'2062-12-2')

insert into Employee values(5,
'Lionel',
'Messi',
'1988-08-21',
'Male',
'Lm10@gmail.com',
'+91 8838902356',
'12, Mission st, Valen, Arg',
'Manager',
'2020-10-2',
'2060-10-2')

create table PayRoll(PayRollId int primary key,
EmployeeId int, 
constraint fk_eId_payRoll foreign key(EmployeeId) references Employee(EmployeeId),
PayPeriodStartDate date,
PayPeriodEndDate date,
BasicSalary decimal(10,2),
OverTimePay decimal(10,2),
Deductions decimal(10,2),
NetSalary decimal(10,2))


insert into PayRoll values(1, 
1, 
'2023-09-01', 
'2023-09-30', 
50000.00, 
10000.00, 
0.00, 
60000.00),
(2, 
2, 
'2023-09-01', 
'2023-09-30', 
50000.00, 
10000.00, 
5000.00, 
55000.00),
(3, 
3, 
'2023-09-01', 
'2023-09-30', 
50000.00, 
10000.00, 
0.00, 
60000.00),
(4, 
4, 
'2023-01-01', 
'2062-12-01', 
100000.00, 
20000.00, 
0.00, 
120000.00),
(5, 
5, 
'2021-01-01', 
'2060-12-01', 
400000.00, 
25000.00, 
0.00, 
425000.00)

create table Tax(TaxId int primary key,
EmployeeId int, 
constraint fk_eId_tax foreign key(EmployeeId) references Employee(EmployeeId),
TaxYear date,
Taxableincome decimal (10,2),
TaxAmount decimal (10,2))

insert into Tax values(1,1,'2024-01-01',50000.00,10000.00),
(2,2,'2024-01-01',50000.00,10000.00),
(3,3,'2024-01-01',50000.00,10000.00),
(4,4,'2024-01-01',100000.00,20000.00),
(5,5,'2024-01-01',400000.00,80000.00)

create table FinancialRecord(RecordId int primary key,
EmployeeId int, 
constraint fk_eId_financialRecord foreign key(EmployeeId) references Employee(EmployeeId),
RecordDate date,
Description varchar(50),
Amount decimal(10,2),
RecordType varchar(20))

insert into FinancialRecord values(1,
1,
'2023-01-01',
'Income Records',
55000.00,
'Income'),
(2,
2,
'2023-01-01',
'Income Records',
53000.00,
'Income'),
(3,
3,
'2023-01-01',
'Expense Records',
13000.00,
'Expense'),
(4,
4,
'2023-01-01',
'Expense Records',
30000.00,
'Expense')

select * from Employee
select * from PayRoll
select * from Tax
select * from FinancialRecord

-- to get all the trainee employees along with their netsalary

select Employee.EmployeeId,Employee.FirstName,Employee.LastName,PayRoll.NetSalary from Employee
join PayRoll on Employee.EmployeeId = PayRoll.EmployeeId where Employee.Position = 'Trainee'

-- to get employee details along with payroll details and taxes for each employee whose netSalary is greater than 45000 and joined on or after 2022

select Employee.*,PayRoll.*,Tax.* from Employee 
join PayRoll on Employee.EmployeeId = PayRoll.EmployeeId 
join Tax on Tax.EmployeeId = Employee.EmployeeId where PayRoll.NetSalary > 45000.00 and Year(Employee.JoiningDate) >= 2022

-- to get the emplpyee details along with deductions whose role is trainee

select Employee.*, PayRoll.Deductions from Employee
join PayRoll on Employee.EmployeeId = PayRoll.EmployeeId 
where PayRoll.Deductions>0 and Employee.Position = 'Trainee'

-- to get employee details, payroll details , tax details along with corresponding records if it exists

select Employee.*,PayRoll.*,Tax.*,FinancialRecord.* from Employee
join PayRoll on Employee.EmployeeId = PayRoll.EmployeeId
join Tax on Employee.EmployeeId = Tax.EmployeeId
join FinancialRecord on Employee.EmployeeId = FinancialRecord.EmployeeId

-- to get the count of employees who are trainee and joined between 2022 and 2024

select count(Employee.EmployeeId) as CountOfEmployees from Employee where JoiningDate between '2022-01-01' and '2024-12-31'

-- to compare the average net salaries of trainee vs manager

select 
(select sum(PayRoll.NetSalary)/(count(PayRoll.EmployeeId)) from PayRoll 
join Employee on PayRoll.EmployeeId = Employee.EmployeeId where Employee.Position = 'Trainee') as AvgTraineeSal,
(select sum(PayRoll.NetSalary)/(count(PayRoll.EmployeeId)) from PayRoll 
join Employee on PayRoll.EmployeeId = Employee.EmployeeId where Employee.Position = 'Manager') as AvgManagerSal

-- to get the employee details along with salary details who works in TN and joined between 2020 and 2024

select Employee.*,PayRoll.* from Employee
join PayRoll on Employee.EmployeeId = PayRoll.EmployeeId
where Employee.Address like '%TN%' and Year(Employee.JoiningDate) between 2020 and 2024

-- to display the income records of employees along with the details

select Employee.*, FinancialRecord.* from Employee
join FinancialRecord on FinancialRecord.EmployeeId = Employee.EmployeeId where FinancialRecord.RecordType = 'Income'

select * from Employee
select * from PayRoll
select * from Tax
select * from FinancialRecord
