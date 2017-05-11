# ![LitReviews](docs/img/LitReviewsBlack@0.5x.png)

# Overview

**LitReviews**, or LitR *(pronounced lighter)*, is a collection of pre-existing tools and custom written scripts to create an **automated** and **systematic** method of conducting **literature reviews in science**. By using **existing APIs** (application programming interfaces), **graph theory**, and **GPU accelerated processing/visualizations**, LitR will hopefully give the user a sense of what ideas, topics, methods, and funding are currently "hot" within a given field of interest.

## Projects

1. [**PubCrawl**](#pubcrawl) - Uses NCBI E-Utilites via BioPython package to search PubMed and pull metadata. Written in Python 3 and visualized in Cytoscape.
2. [**PubCrawlR**](#pubcrawlr) - Future development. Will likely be an extension to PubCrawl which uses R for statistical analyses on metadata.
3. [**CrossCheck**](#crosscheck) - Future development. Citation metadata and funding analyzer using NIH RePORTER (or CrossRef as suggested by Ben Wilks).

Please see [works referenced](#works-referenced) for information about the original works on which LitR builds upon.

## Examples

Check out an example and look for tutorials [here](./examples/)

# Getting Started

1. Read the [PubMed Guidelines for Scripting Calls](./third_party_licenses/NCBI_Disclaimer.md)

## Dependencies

- BioPython

# PubCrawl

![](docs/img/PubCrawl@0.5x.png)

# PubCrawlR

![](docs/img/PubCrawlR@0.5x.png)

# CrossCheck

![](docs/img/CrossCheck-02@0.5x.png)

# Works Referenced
[Back to top](#overview)

* [BioPython](https://github.com/biopython/biopython)
    * Cock, P.J.A. et al. Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics 2009 Jun 1; 25(11) 1422-3 http://dx.doi.org/10.1093/bioinformatics/btp163 pmid:19304878

* [CytoScape](http://www.cytoscape.org/)
    * Shannon P, Markiel A, Ozier O, Baliga NS, Wang JT, Ramage D, Amin N, Schwikowski B, Ideker T. Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome Research 2003 Nov; 13(11):2498-504

* [NCBI](https://www.ncbi.nlm.nih.gov/Structure/flink/flink.cgi)
    * FLink: Frequency weighted links [Internet]. Bethesda (MD): National Library of Medicine (US), National Center for Biotechnology Information. 2010. Available from: https://www.ncbi.nlm.nih.gov/Structure/flink/flink.cgi

* [CentiScape](https://bitbucket.org/giovanniscardoni/centiscapepublic)
    * Scardoni G, Tosadori G, Faizan M, Spoto F, Fabbri F, Laudanna C. Biological network analysis with CentiScaPe: centralities and experimental dataset integration. F1000Research. 2014;3:139. doi:10.12688/f1000research.4477.2.

# Artwork

Logos designed and created by Adewole C. Oyalowo using icons provided free by [EmojiOne](http://emojione.com/).
