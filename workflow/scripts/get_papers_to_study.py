"""This script creates a list of DOIs for papers to be incldued in analysis in this project

input: vispd_plus_good_papers

output: papers_to_study

procedure: to exclude the nine DOIS that are inaccessible in OpenAlex

"""

import pandas as pd
import csv
import sys

VISPD_PLUS_GOOD_PAPERS = sys.argv[1]
PAPERS_TO_STUDY = sys.argv[2]

def read_txt(INPUT):
    """read txt files and return a list
    """
    raw = open(INPUT, "r")
    reader = csv.reader(raw)
    allRows = [row for row in reader]
    data = [i[0] for i in allRows]
    return data

def get_papers_to_study(INPUT): # INPUT here is vispd_plus_good_papers
    vispd_plus_good_papers = read_txt(INPUT)
    to_exclude_from_analysis = [
        '10.1109/VISUAL.1994.346342',
        '10.1109/VISUAL.1992.235201',
        '10.1109/VISUAL.1991.175770',
        '10.1109/VISUAL.1990.146412',
        '10.1109/VISUAL.1991.175830',
        '10.1109/VISUAL.1992.235180',
        '10.1109/tvcg.2020.3032123',
        '10.1109/VISUAL.2003.1250379',
        '10.1109/TVCG.2014.2346442',
    ]
    papers_to_study = [
        x for x in vispd_plus_good_papers if x not in to_exclude_from_analysis
    ]
    return papers_to_study

papers_to_study = get_papers_to_study(VISPD_PLUS_GOOD_PAPERS)

with open(PAPERS_TO_STUDY, 'w') as f:
    for doi in papers_to_study:
        f.write("%s\n" % doi)