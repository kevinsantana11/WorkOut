USE [WorkOut_Db]
GO

CREATE PROCEDURE usp_InsertMuscles
(
	@muscleId INT,
	@muscleName VARCHAR(255)
)
AS
INSERT INTO [dbo].[Muscles]
           (Id
           ,Name)
     VALUES
           (
				 @muscleId
				,@muscleName
		   )
GO


