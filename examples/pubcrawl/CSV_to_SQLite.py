import sys
import numpy as np
import pandas as pd
import sqlite3 as sql
import ast

# from sklearn import linear_model

strDir = './output/'
strCSVFile = '20170322_pmid_summaries_concussion.csv'
# Set the name of the CSV file to arg if possible
# if len(sys.argv) > 1:
#     strCSVFile = sys.argv[1]

df = pd.read_csv(strDir + strCSVFile, parse_dates=[4,18,23]) # 4, 18, 23 are dates
df['PubDate'] = pd.to_datetime(df['EPubDate'], errors='coerce')
df['PubDate'] = pd.to_datetime(df['PubDate'], errors='coerce')
df['SO'] = pd.to_datetime(df['SO'], errors='coerce')

df = pd.DataFrame(df[0:100], copy=True)

print(df.head)
print(df.PubDate.dt.day)

strID = df.ArticleIds.values[0]
v = ast.literal_eval(strID)
# print(v)

# CREATE TABLE "demo" ("id" integer, "gender"  text, "age"  text)

strSQLFile = './test.sqlite'
conn = sql.connect(strSQLFile)
c = conn.cursor()

# Add Papers table
strSQL = 'DROP TABLE IF EXISTS "tblPapers";'
c.execute(strSQL)
strSQL = 'CREATE TABLE "tblPapers" (\
            "Paper_ID" INTEGER PRIMARY KEY AUTOINCREMENT, \
            "Title" TEXT \
            );'
#             "pubmed" INTEGER, "medline" TEXT, "pii" TEXT, "doi" TEXT, "rid" INTEGER, "eid" INTEGER\
c.execute(strSQL)

# Add Authors table
strSQL = 'DROP TABLE IF EXISTS "tblAuthors";'
c.execute(strSQL)
strSQL = 'CREATE TABLE "tblAuthors" (\
            "Author_ID" INTEGER PRIMARY KEY AUTOINCREMENT, \
            "Paper_ID" INTEGER, "Author" TEXT \
            );'
#             "pubmed" INTEGER, "medline" TEXT, "pii" TEXT, "doi" TEXT, "rid" INTEGER, "eid" INTEGER\
c.execute(strSQL)

for row in df.itertuples(index=False, name='Pandas'):

#     print(row.ArticleIds)
#     vIDs = ast.literal_eval(row.ArticleIds)

    # Add each paper to the Papers table
    strSQL = ( "INSERT INTO \"tblPapers\" \
            (\"Title\") \
            VALUES (\"%s\");" % (row.Title.replace("\"","")) )

#     print(strSQL)
    c.execute(strSQL)

    # For each author in the paper, add the author into the Authors table
    iPaperID = c.lastrowid
    vAuthors = ast.literal_eval(row.AuthorList)
    for strAuthor in vAuthors:
        strSQL = ( "INSERT INTO \"tblAuthors\" \
            (\"Paper_ID\", \"Author\") \
            VALUES (%d, \"%s\");" % (iPaperID, strAuthor) )

        print(strSQL)
        c.execute(strSQL)
        print(c.lastrowid)

conn.commit()
conn.close()