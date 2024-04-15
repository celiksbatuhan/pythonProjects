import sqlite3


def customersNames():
    connection = sqlite3.connect("sqliteDemo.db")

    cursor = connection.execute("select FirstName,LastName from Customers")
    print("-----------------------")

    for row in cursor:
        print("•" + "FirstName =", row[0])
        print("•" + "LastName =", row[1])
        print("-----------------------")

    connection.close()

#customersNames()

def countOfCountries():
    connection = sqlite3.connect("sqliteDemo.db")
    cursor = connection.execute("select Country, count(*) from Customers group by Country order by count(*) desc")
    print("-----------------------")

    for row in cursor:
        print("•" + "Country =", str(row[0]))
        print("•" + "Count =", str(row[1]))
        print("-----------------------")

    connection.close()

#countOfCountries()

def alphabeticalOrder():
    connection = sqlite3.connect("sqliteDemo.db")
    cursor = connection.execute("""
    select FirstName,LastName from Customers where FirstName like 'a%'
    """)
    print("-----------------------")

    for row in cursor:
        print("•" + "FirstName =", row[0])
        print("•" + "LastName =", row[1])
        print("-----------------------")

    connection.close()

#alphabeticalOrder()

def insertCustomer():
    connection = sqlite3.connect("sqliteDemo.db")
    connection.execute("""
    insert into Customers (CustomerId, FirstName, LastName, City, Country, Email) 
    values ('60', 'Batuhan Osman', 'Çelik', 'İstanbul', 'Türkiye', 'batuhanosman.celik@gmail.com')
    """)
    connection.commit()
    connection.close()

#insertCustomer()

def updateCustomer():
    connection = sqlite3.connect("sqliteDemo.db")
    connection.execute("""
    update customers set Country='Romania', City='Iaşi' where Country='Türkiye' and City='İstanbul'
    """)
    connection.commit()
    connection.close()

#updateCustomer()

def deleteCustomer():
    connection = sqlite3.connect("sqliteDemo.db")
    connection.execute("""
    delete from customers where CustomerId=60
    """)
    connection.commit()
    connection.close()

#deleteCustomer()

def selectionOperations():
    connection = sqlite3.connect("sqliteDemo.db")

    cursor = connection.execute("""
    SELECT artists.Name, albums.Title FROM artists INNER JOIN albums
    on artists.ArtistId = albums.ArtistId
    """)
    print("-----------------------")

    for row in cursor:
        print("•" + "Name =", row[0])
        print("•" + "Title =", row[1])
        print("-----------------------")

    connection.close()

#selectionOperations()