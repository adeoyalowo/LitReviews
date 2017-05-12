# Background

## Problem

Our project is a metastudy of research into Chronic Traumatic Encephalopathy (CTE). We are hoping to determine whether the number of times a paper is cited can be predicted with any degree of accuracy using features of the article.
That is, are papers on this topic more likely to be cited strictly based on their content or on more extraneous features, such as publication date or the presence of a well-known author?

## Data

The data are all provided by the PubMed API.
A Python program (written by Ade as part of his broader work on this subject) creates a CSV file collecting metadata for all articles that match a given keyword (Title, PubMed ID, Authors, Date, Language, etc...).

The next program converts the data from the CSV file into a SQLite database.

Finally, a third program loads data from the database, converts it to NumPy matrices, and uses learning algorithms to make predictions about papers and their citations.

# Complications

## Complexity

The PubMed API produces a dataset that contains a large number of values, some of which are duplicated in various ways. These values must be culled, reformatted, and reorganized.
The data are also highly inconsistent:
* Some unique ID's are all unsigned integers, while others contain dashes and other characters. This means that some IDs can be treated as numeric values, while others must be treated as text strings.
* There are several date fields marking different milestones in the publication process, but they are formatted in different ways. Some are missing the day and even the month (older citations from the 19th century tend to only record the year), while others have a full timestamp including a (presumably arbitrary) time of publication.
* The most disappointing setback we faced was determining page numbers and, as a result, article length. The information about page numbers is ostensibly included in the search results, which would theoretically make it possible to calculate article length. However, the quality of these data is so low that it would only be possible to process it accurately in 30-40% percent of cases (by rough estimation). If there were a way to calculate article length, that value could be compared with other metrics in potentially illuminating ways. For example, are short articles likely to have fewer citations? It might eventually be possible to gather this information in other ways (for instance, by scraping the PubMed site directly and counting the number of page images shown), but for now that value is unobtainable.

## Computation

At all stages of the project, computational complexity remained in the foreground of our considerations. The decision to create multiple programs that would store and retrieve data from a SQLite database was partially motivated by a desire to separate the overall process into multiple steps so that computationally intensive data processing operations could be done individually and the results saved in a database for later use. This approach offers a number of advantages, but in particular it prevents the machine learning algorithm from facing a data processing bottleneck each time it is run.

## Drawbacks of Standard Methods

Issues of computational complexity also extend to the choice of problem-solving approach and the variety of different machine learning techniques available to us.
For example, to track the many-to-many relationship between authors and papers, it is theoretically possible to create an adjacency matrix in which each paper is assigned a row and each author a column and binary values indicate whether a given author worked on a given paper:

*Paper 1* by Bob, Charles, and David

*Paper 2* by Alice and Charles

*Paper 3* by Alice and David

|         	| Alice 	| Bob 	| Charles 	| David 	|
|---------	|-------	|-----	|---------	|-------	|
| Paper 1 	| 0     	| 1   	| 1       	| 1     	|
| Paper 2 	| 1     	| 0   	| 1       	| 0     	|
| Paper 3 	| 1     	| 0   	| 0       	| 1     	|
However, with the numbers of papers and authors in the tens of thousands, and most papers having one author and most authors having only a single paper, this matrix would be enormous and sparse.

## Visualization

The size of the dataset makes visualization a special challenge.

![](../../docs/img/citationgraph.png)

