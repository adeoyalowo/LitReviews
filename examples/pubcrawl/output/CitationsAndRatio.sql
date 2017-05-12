SELECT Cited, 
	SUM(Internal) AS `InternalCitations`, 
	COUNT(Internal) AS `TotalCitations`, 
	CAST(SUM(Internal) AS FLOAT)/CAST(COUNT(Internal) AS FLOAT) AS `Ratio` 
		FROM tblCitations GROUP BY Cited 
ORDER BY Ratio DESC, InternalCitations DESC