# Table of Contents
1. [Introduction]
2. [Input/Output]
3. [Code implementation]
4. [Repo directory structure]


# Introduction

This project is the implementation of InsightDataScience's coding challenge "Donation Analytics". Detailed description please refer to https://github.com/InsightDataScience/donation-analytics


# Input/Output

1. Input file "percentile.txt" holds a single value -- the percentile value (1-100) that the program is asked to calculate.
2. Input file "itcont.txt" has a line for each campaign contribution that was made on a particular date from a donor to a political campaign, committee or other similar entity. 
3. Output file "repeat-donors.txt" lists the running statistics of contributions from repeated donors for that recipient, zip code and year 


# Code implementation
1. data_validation.py is screening the data per requirement of this project. Transaction that has invalid input will be ignored in the data processing
2. Donation-analytics.py is the main coding file that conducts the data analysis.
3. python modules needed: math, datetime, sys, sortedcontainers


# Repo directory structure

    ├── README.md 
    ├── run.sh
    ├── src
    │	└── data_validation.py
    │   └── donation-analytics.py
    ├── input
    │   └── percentile.txt
    │   └── itcont.txt
    ├── output
    |   └── repeat_donors.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── percentile.txt
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── repeat_donors.txt
            ├── selftest
                ├── input
                │   └── percentile.txt
                │   └── itcont.txt
                |── output
                    └── repeat_donors.txt

