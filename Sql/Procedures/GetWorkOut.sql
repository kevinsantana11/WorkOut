CREATE PROCEDURE usp_GetWorkOut
(
	@workOutId AS INT
)
AS
	SELECT
		wo.workOutName
	FROM dbo.WorkOut as wo
	WHERE wo.workOutId = @workOutId;
	GO