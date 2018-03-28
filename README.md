# Poppins

## Pre-requisites

You will need python>=3.6 and zsh>=5.4. If you also wish to perform the image
stitching in the same way that we have then you will also require
ImageMagick>=7.0.7.

In order to run the python code used in the manipulation of the reports you
should install the pre-requisite modules using pip with `requirements.txt`:

``` sh
pip3 install -r requirements.txt
```

## Instructions for use

#### Preparation

First clone this repository
``` sh
git clone git@github.com:datasciencecampus/poppins
```

#### Usage

All of the functionality is available through `poppins`, the
help for which you can access by using
``` sh
./poppins -h
```
or
``` sh
./poppins --help
```

It is also printed when you call the program with no flags.


This program will allow you to
+ clean the report data after it has been converted from pdf to plain text
+ structure the data into a CSV file and a SQLite3 database
+ generate some basic wordclouds to understand report sections by rating
+ perform TF-IDF calculations
