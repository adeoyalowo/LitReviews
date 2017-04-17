"""
This script provides a GUI for using the BioPython API, NCBI e-utilites, and NCBI FLink.

Author: Adewole C. Oyalowo
email: adewole_oyalowo@brown.edu
Please see license file for information on modificaiton or distribution.
"""

import os
import sys
from PyQt5 import QtGui, uic, QtWidgets, QtCore
from LitReviews.pubcrawl.ui.pubcrawl_ui import Ui_MainWindow
from LitReviews.pubcrawl import bputils
import pandas as pd
import numpy as np

class PubCrawlApp(Ui_MainWindow):

    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.output = os.path.join(os.path.dirname(__file__),"LitReviews","pubcrawl","output")
        self.fileSystemModel = QtWidgets.QFileSystemModel(self.treeView)
        root = self.fileSystemModel.setRootPath(self.output)
        self.fileSystemModel.setReadOnly(False)
        self.treeView.setModel(self.fileSystemModel)
        self.treeView.setRootIndex(root)
        self.initActions()
        self.show()

    def initActions(self):
        self.emailButton.clicked.connect(self.set_email)
        self.searchButton.clicked.connect(self.search)
        self.summariesButton.clicked.connect(self.generate_summaries)
        self.pmidsButton.clicked.connect(self.ui_list)

    def set_email(self):
        bputils.Entrez.email = self.emailQle.text()
        bputils.Entrez.tool = "pubcrawl via biopython"
        self.statusbar.showMessage('email set to {}'.format(bputils.Entrez.email))

    def search(self):
        self.searchTerm = self.searchTermQle.text()
        self.searchTermQle.clear()
        self.previousSearchTermLabelName.setText(self.searchTerm)

        pmCount, pmcCount = bputils.info(self.searchTerm)

        self.pmRefCountLabel.setText("Pm Ref Count: {}".format(pmCount))
        self.pmcRefCountLabel.setText("Pmc Ref Count: {}".format(pmcCount))

        self.searchResults = bputils.search(self.searchTerm)

    def generate_summaries(self):
        count = int(self.searchResults['Count'])
        batchSize = 100

        with open(os.path.join(self.output,"summaries.csv"), "w") as outfile:

            writeHeader = True
            for start in range(0,count,batchSize):
                end = min(count, start+batchSize)
                self.statusbar.showMessage("Going to download record {} to {} of {}".format(start+1, end, count))
                self.progressBar.setValue(int((((end+1)/count)*100)))
                attempt = 0

                try:
                    summaryResults = bputils.summary(self.searchResults,start,batchSize)

                    metadata = [dict(metainfo) for metainfo in summaryResults]
                    df = pd.DataFrame(metadata)

                    df.to_csv(outfile, index=False, header=writeHeader)
                    writeHeader = False

                # TODO: Handle HTTP errors.
                except Exception as err:
                    print(err)

        self.statusbar.showMessage("Summaries task complete.")
        self.progressBar.setValue(100)

    def ui_list(self):

        count = int(self.searchResults['Count'])
        batchSize = 100

        with open(os.path.join(self.output,"uilist.txt"), "a") as outfile:

            writeHeader = True
            for start in range(0,count,batchSize):
                end = min(count, start+batchSize)
                self.statusbar.showMessage("Going to download record {} to {} of {}".format(start+1, end, count))
                self.progressBar.setValue(int((((end+1)/count)*100)))
                attempt = 0

                try:

                    fetchResults = bputils.fetch(self.searchResults,start,batchSize)
                    outfile.write(fetchResults)

                # TODO: Handle HTTP errors.
                except Exception as err:
                    print(err)

            self.statusbar.showMessage("UI List Complete.")
            self.progressBar.setValue(100)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = PubCrawlApp()
    sys.exit(app.exec_())
