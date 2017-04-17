"""
Author: Adewole C. Oyalowo
email: adewole_oyalowo@brown.edu
This script uses the BioPython API of the NCBI e-utilites to retrieve requested info.
Please see license file for information on modificaiton or distribution.
"""

from Bio import Entrez

def info(searchTerm):
    egqHandle = Entrez.egquery(term=searchTerm)
    egqRecord = Entrez.read(egqHandle)
    egqHandle.close()
    pmCount = egqRecord["eGQueryResult"][0]["Count"]
    pmcCount = egqRecord["eGQueryResult"][1]["Count"]
    return pmCount, pmcCount

def search(searchTerm):
    searchHandle = Entrez.esearch(
                                    db='pubmed',
                                    term=searchTerm,
                                    retmax=0,
                                    retstart=0,
                                    sort='relevance',
                                    usehistory='y',
                                 )

    searchResults = Entrez.read(searchHandle)
    searchHandle.close()

    return searchResults

def summary(searchResults, start, batchSize):

    summaryHandle = Entrez.esummary(
                                    db='pubmed',
                                    query_key=searchResults['QueryKey'],
                                    WebEnv=searchResults['WebEnv'],
                                    retstart=start,
                                    retmax=batchSize,
                                    )

    summaryResults = Entrez.read(summaryHandle)
    summaryHandle.close()

    return summaryResults

def fetch(searchResults,start,batchSize):
    fetchHandle = Entrez.efetch(
                                    db='pubmed',
                                    rettype='uilist',
                                    query_key=searchResults['QueryKey'],
                                    WebEnv=searchResults['WebEnv'],
                                    retstart=start,
                                    retmax=batchSize,
                                    )


    fetchResults = fetchHandle.read()
    fetchHandle.close()

    return fetchResults
