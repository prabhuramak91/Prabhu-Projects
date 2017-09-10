

```python
Summer 2017

MIS 6V99 – Special Topics – Programming for Data Science

Social Media Analytics – given a file of Twitter events in JSON format, perform some simple analytics on the Tweets




Scenario


We have a file of Twitter events in JSON format. We want to read in the Twitter events and perform some basic analytics on them.




Download the JSON file of Twitter events

Your Python program should download the JSON file of Twitter events from the following link:

http://kevincrook.com/utd/tweets.json

Your Python program should read this file into Python data structures for analytics.




Create the analytics files


You Python program will create a file of various twitter analytics in the local directory called twitter_analytics.txt

Do not create a header record for this file.

The file must be a proper text file using utf-8 encoding, with each line (including the last line) properly terminated by a machine independent end of line character.

The first line of the file should have the total number of events. The number should be on the line by itself, without a label, and without leading zeroes.

The next line of the file should be the total number of Tweets. For the purposes of this assignment, assume that if a Twitter event has a ‘text’ attribute, it is a Tweet. The number should be on the line by itself, without a label, and without leading zeroes.

Considering only Tweets, count the frequency of Tweets for each language. Sort by highest frequency first. For each language, write it’s 2 letter lower case abbreviation, followed by a comma, followed by the frequency on a line. The frequency should be a number without any leading zeroes. No spaces!
 



MIS 6V99 – Special Topics – Programming for Data Science – Programming Assignment #4	page 1 of 5
 
Create the Tweets files


You Python program will create a file of Tweet texts in the local directory called tweets.txt

Do not create a header record for this file.

The file must be a proper text file using utf-8 encoding, with each line (including the last line) properly terminated by a machine independent end of line character.

Each line will be 1 Tweet text. For the purposes of this assignment, assume that if a Twitter event has a ‘text’ attribute, it is a Tweet. They should be in the same order as the input file.

Hint: There will be Tweets in various languages, many will require Unicode, and many will have Unicode

characters that cannot be printed in English (Latin-1). Be sure you file is text with utf-8 encoding. You will see

characters such as these:

\uc0ac\uc0c1\ucd9c\uc7a5\uc548\ub9c8

```
