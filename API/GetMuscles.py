import requests
import json
import pyodbc

connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-HRIJH4E;"
                      "Database=WorkOut_Db;"
                      "Trusted_Connection=yes;")

cursor = connection.cursor()

request = requests.get("https://wger.de/api/v2/muscle/")


jsonMuscles = json.loads(request.text);

muscles = jsonMuscles["results"]


for muscle in muscles:
    muscleId = muscle["id"]
    muscleName = muscle["name"]
    executeStatement = "EXECUTE dbo.usp_InsertMuscles %d, '%s'" % (muscleId, muscleName)
    cursor.execute(executeStatement)


connection.commit()





