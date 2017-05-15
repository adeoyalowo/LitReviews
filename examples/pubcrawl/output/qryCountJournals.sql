SELECT COUNT(tblPapers.FullJournalName) AS `NumArticles` 
FROM tblPapers 
GROUP BY tblPapers.FullJournalName
ORDER BY NumArticles DESC
