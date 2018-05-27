ALTER PROCEDURE usp_InsertExercise
(
	 @exerciseName			VARCHAR(255)
	,@exerciseDescription	VARCHAR(255)
	,@primaryMuscles		VARCHAR(255)
	,@secondaryMuscles		VARCHAR(255)
)
AS
DECLARE @primaryMuscleId VARCHAR(255);
DECLARE @secondaryMuscleId VARCHAR(255);
DECLARE @commaIndex INT = 0;
DECLARE @stringLength INT = 0;
DECLARE @primaryUnique VARCHAR(255) = NEWID();
DECLARE @secondaryUnique VARCHAR(255) =  NEWID();
SET @primaryMuscleId = @primaryMuscles;
SET @secondaryMuscleId = @secondaryMuscles;

INSERT INTO [dbo].[Exercise]
(
	[name]
   ,[PrimaryMuscleGroupId]
   ,[SecondaryMuscleGroupId]
   ,[Description]
)
VALUES
(
	 @exerciseName
	,@primaryUnique
	,@secondaryUnique
	,@exerciseDescription
)


	WHILE(@primaryMuscleId  IS NOT NULL)
		BEGIN
			SET @commaIndex =  PATINDEX('%,%', @primaryMuscleId);
			SET @stringLength = LEN(@primaryMuscleId) - @commaIndex;
			SET @commaIndex =  @commaIndex + 1;

			SELECT SUBSTRING(@primaryMuscleId, 1, 1) as string;
			INSERT INTO [dbo].[MuscleGroups]
            (
				 [MuscleGroupdId]
				,[MuscleId]
		    )
			VALUES
            (
				 @primaryUnique
				,CAST(SUBSTRING(@primaryMuscleId, 1, 1) AS INT)
			)
			IF(@commaIndex = 1)
				BEGIN
					SET @primaryMuscleId = NULL; 
				END;
			ELSE
				BEGIN
					SET @primaryMuscleId = SUBSTRING(@primaryMuscleId, @commaIndex, @stringLength);
				END;
		END;
		WHILE(@secondaryMuscleId  IS NOT NULL)
		BEGIN
			SET @commaIndex =  PATINDEX('%,%', @secondaryMuscleId);
			SET @stringLength = LEN(@secondaryMuscleId) - @commaIndex;
			SET @commaIndex =  @commaIndex + 1;

			SELECT SUBSTRING(@secondaryMuscleId, 1, 1) as string2;
			INSERT INTO [dbo].[MuscleGroups]
            (
				 [MuscleGroupdId]
				,[MuscleId]
		    )
			VALUES
            (
				 @secondaryUnique
				,CAST(SUBSTRING(@secondaryMuscleId, 1, 1) AS INT)
			)
			IF(@commaIndex = 1)
				BEGIN
					SET @secondaryMuscleId = NULL; 
				END;
			ELSE
				BEGIN
					SET @secondaryMuscleId = SUBSTRING(@secondaryMuscleId, @commaIndex, @stringLength);
				END;
		END;