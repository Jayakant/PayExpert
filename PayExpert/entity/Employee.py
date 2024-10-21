class Employee():
    def __init__(self,employeeId, firstName, lastName, dateOfBirth, gender, email,
                phoneNumber, address, position, joiningDate, terminationDate):
        self.employeeId = employeeId
        self.firstName = firstName
        self.lastName = lastName
        # self.dateOfBirth = datetime.strptime(dateOfBirth, "%Y-%m-%d").date()
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
        self.position = position
        self.joinigDate = joiningDate
        self.terminationDate = terminationDate
        # self.joiningDate = datetime.strptime(joiningDate, "%Y-%m-%d").date()
        # self.terminationDate = datetime.strptime(terminationDate, "%Y-%m-%d").date()