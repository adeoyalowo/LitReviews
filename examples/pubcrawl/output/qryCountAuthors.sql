SELECT COUNT(tblAuthors.Author) AS `NumAuthors` 
FROM tblAuthors 
INNER JOIN tblPapers ON tblAuthors.Paper_ID = tblPapers.Paper_ID
GROUP BY tblAuthors.Author
ORDER BY NumAuthors DESC
