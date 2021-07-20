from tkinter import filedialog
import os
import sqlite3
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData 
def insertBLOB(empId, name, photo):
    try:
        sqliteConnection = sqlite3.connect('foto.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (id, name, photo) VALUES (?, ?, ?)"""
        

        empPhoto = convertToBinaryData(photo)
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(empId):
    try:
        sqliteConnection = sqlite3.connect('foto.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee"""
        cursor.execute(sql_fetch_blob_query)
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            #resumeFile = row[3]

            print("Storing employee image and resume on disk \n")
            dir_path = os.path.dirname(os.path.realpath(__file__))

            photoPath = dir_path +'\cache'+'\\'+ name +'$'+str(row[0])+ ".jpg"
            writeTofile(photo, photoPath)
            #writeTofile(resumeFile, resumePath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
"""teste=[]
bd = sqlite3.connect('foto.db')
cursor = bd.cursor()
motos = CREATE TABLE IF NOT EXISTS new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL);
cursor.execute(motos)
bd.commit()
bd.close()
arquivos=filedialog.askopenfilenames()
teste.append(arquivos)
insertBLOB(1,'testando',arquivos[0])
readBlobData(1)
#cursor.execute(motos)
codigo = 123
print(arquivos)"""