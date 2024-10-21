class DBPropertyUtil: 
    @staticmethod
    # def getConnectionStr(driver,server,database,trustedConnection):
    def getConnectionStr():
        driver = "ODBC Driver 17 for SQL Server"
        server = "hpVic\\SQLEXPRESS"
        database = "payExpert"
        trustedConnection = "yes"
        
        connStr = f"Driver={{{driver}}};Server={server};Database={database};Trusted_Connection={trustedConnection};"
        return connStr