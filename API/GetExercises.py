import requests
import json
import pyodbc
import re


def turn_array_to_string(array):

    array_length = len(array)
    i = 0
    string_to_return = ""

    while i < array_length:
        string_to_return += str(array[i])
        if i < array_length - 1:
            string_to_return += ","
        i += 1
    return string_to_return


connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=DESKTOP-HRIJH4E;"
                            "Database=WorkOut_Db;"
                            "Trusted_Connection=yes;")

cursor = connection.cursor()

muscle = 1

while muscle <= 15:

    request = requests.get("https://wger.de/api/v2/exercise/?status=2&language=2&muscles=%d" % muscle)
    exerciseJSON = json.loads(request.text)
    exercises = exerciseJSON["results"]

    print()
    print("muscle - %d" % muscle)
    print()

    muscle += 1

    for exercise in exercises:
        exerciseName = exercise["name"]
        exerciseDescription = exercise["description"]
        exerciseMuscles = exercise["muscles"]
        exerciseSecondaryMuscles = exercise["muscles_secondary"]

        exerciseName = re.sub("'", "", exerciseName)
        exerciseDescription = re.sub("'", "", exerciseDescription)
        primaryMuscles = turn_array_to_string(exerciseMuscles)
        secondaryMuscles = turn_array_to_string(exerciseSecondaryMuscles)

        executeStatement = "EXECUTE dbo.usp_InsertExercise '%s', '%s', '%s', '%s'" % (exerciseName, exerciseDescription, primaryMuscles, secondaryMuscles)
        print(executeStatement)
        cursor.execute(executeStatement)

    nextPage = exerciseJSON["next"]

    while nextPage is not None:
        print()
        print("Next Page")
        print()
        request = requests.get(nextPage)
        exerciseJSON = json.loads(request.text)
        nextPage = exerciseJSON["next"]

        exercises = exerciseJSON["results"]

        for exercise in exercises:
            exerciseName = exercise["name"]
            exerciseDescription = exercise["description"]
            exerciseMuscles = exercise["muscles"]
            exerciseSecondaryMuscles = exercise["muscles_secondary"]

            exerciseName = re.sub("'", "", exerciseName)
            exerciseDescription = re.sub("'", "", exerciseDescription)
            primaryMuscles = turn_array_to_string(exerciseMuscles)
            secondaryMuscles = turn_array_to_string(exerciseSecondaryMuscles)

            executeStatement = "EXECUTE dbo.usp_InsertExercise '%s', '%s', '%s', '%s'" % (exerciseName, exerciseDescription, primaryMuscles, secondaryMuscles)
            print(executeStatement)
            cursor.execute(executeStatement)

connection.commit()





