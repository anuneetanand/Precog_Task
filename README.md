# Precog Recruitment Tasks


## Folder Structure
```
├── README.md
├── Task_1
│   └── Paper_Summary.pdf
├── Task_2
│   ├── Dump
│   │   ├── Raw_Tweets.json
│   │   ├── Top_HashTags.json
│   │   ├── Tweets.json
│   │   └── Users.json
│   │   └── App
│   ├── Scripts
│   │   ├── Data_Extraction.py
│   │   └── Raw_Data_Collection.py
│   ├── Tweet_Analysis.ipynb
│   └── Tweet_Analysis.pdf
├── Task_3
│   ├── A
│   │   ├── Files
│   │   ├── MongoDump
│   │   ├── Script.py
│   │   ├── TableExtraction.ipynb
│   │   └── TableExtraction.pdf
│   └── B
│       ├── Parse_XML.py
│       ├── Report.pdf
│       ├── StackOverflowEDA.ipynb
│       └── StackOverflowEDA.pdf
└── requirements.txt
```


## Task 1

Summarised the paper : [How Community feedback shapes users behaviour](https://cs.stanford.edu/people/jure/pubs/disqus-icwsm14.pdf)


## Task 2

Top HashTag in Delhi : `#HappyNewYear`

- `Raw_Data_Collection.py` : Identify top HashTag and collect 10000 tweets around the top HashTag.
- `Data_Extraction.py` : Clean the Raw JSON dumps of tweets and generate dumps which can be loaded directly as Dataframes.
- `Tweet_Analysis.ipynb` : Analysis of Tweets and Users. 

## Task 3

## A

- `Script.py` : Given path to local pdf file location, captures the tables and stores them as in the same location.
- `TableExtraction.ipynb` : The generalised script did not perform well for the files provided. Hence I tweaked it and tried to get best results for each file. The results are given as MongoDB dump.

## B

- `Parse_XML.py` : Parses the XML files and stores them in the MongoDB Database as a collection. [Drive Link](https://drive.google.com/drive/folders/1-CzccA6Kwzn3nUrFHDErRqPVhS4cyhdr?usp=sharing)
- `StackOverflowEDA.ipynb` : Exploratory Data Analysis on Stack Overflow Data.

## Loading MongoDump

Go to the approproate folders and run the following commands on the shell.

```mongorestore PDF_Extraction```

```mongorestore StackOverflowDB```

## Required Packages

``` pip install -r requirements.txt ```
