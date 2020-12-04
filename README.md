# Election Analysis
**Project Overview**
 \
This project uses Python to analyze 369,712 ballets and determine:
 \
1. the winner of a Colorado election, 
2. the proportion and number of votes that each candidate won,
3. the proportion and number of votes that each county cast.
 \
**Results**
\
Three contestents and three counties competed in the election. A total of 369,712 voters participated. The winner was Diana DeGette. She won 73.8% of the vote with 272,892 ballets. Charles Stockham came in second (23% of the vote). Raymon Doane brought up the rear (3.1% of the vote). Denver county submited the most ballets (306,055). This means it had nearly 8x more voters than Jefferson or Arapahoe County.\
**Recommendations**
 \
To use the script at scale, the following checks are recommended:
 \
A. Make sure to capture a distinct list, such as each candidate.\
For example:
This code uses if statements to achieve a distinct count.\
!["Distinct_Count"](https://github.com/dagibbins186/Election_Analysis/blob/main/Images/Distinct_Count.png)
Here the "if candidate_name not in candidate_options" line renders the distinct name. 
B. Total all the values inside a list
To count all the elements inside of a list, a for loop is used. The code initializes the count variable (votes) to 0 and loops through the list (e.g. candidate name). 
!["Total_Vote"](https://github.com/dagibbins186/Election_Analysis/blob/main/Images/Total_Vote.png)
In every loop iteration, the number of votes increases by the candidate name.
!["For_Statement"](https://github.com/dagibbins186/Election_Analysis/blob/main/Images/For_Statement.png)
Some modifications could also help to make the results clearer. For instance, with more counties, it may be worthwhile to state the total number of counties participating, not list them. Then, the results could just show the top three counties. As the data set increases, summaries that show the key results, not all of the results, will help the reader. 
