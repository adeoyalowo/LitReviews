SELECT *, SUM(Internal) AS `InternalCitations`, COUNT(Internal) AS `TotalCitations` FROM tblPapers
LEFT JOIN tblCitations ON tblPapers.Id = tblCitations.Cited
GROUP BY Id
ORDER BY TotalCitations DESC