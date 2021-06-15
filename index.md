# Statistical Distributions

## Question 1

**Use the following information to determine your answers for questions 1 and 2:**

> The typicle adult male shoe size has a bell shaped distribution with a mean of 10.5 and a standard deviation of 1.3.

About 68% of adult men typically have a shoe size between a minimum of  ________ and a maximum of _____________

Please assign your answer to the variable `question_1`, with a datatype of `tuple`, rounded to the first decimal place, and with the following format:

`(min_value, max_value)`


```python
# Your answer here
```

## Question 2

Suppose Johnny has a shoe size of 8. How many standard deviations are they from the mean? Please round to the second decimal point. Assign your answer to the variable `question_2`


```python
# Your answer here
```

## Question 3

**For the next three questions, use the following information to determine your answers:** 

A psychology experiment on memory was conducted which required participants to recall anywhere from 1 to 10 pieces of information. Based on many results, the (partial) probability distribution below was determined for the discrete random variable (X = number of pieces of information remembered (during a fixed time period)).

What is the missing probability `P(X=7)`? Your answer should be rounded to the second decimal, and assigned to the variable `question_3`.

| X = # of information 	| 1   	| 2    	| 3    	| 4    	| 5    	| 6    	| 7 	| 8    	| 9    	| 10   	|
|----------------------	|-----	|------	|------	|------	|------	|------	|---	|------	|------	|------	|
| Probability          	| 0.0 	| 0.02 	| 0.04 	| 0.07 	| 0.15 	| 0.18 	| ? 	| 0.14 	| 0.11 	| 0.05 	|



```python
# Your answer here
```

## Question 4
Using probabilities from the above table, complete the table below to provide the cumulative distribution function of X.

Please assign your answer to the variable `question_four` and format your response in the following way:

(val_one, val_two, val_three, val_four, val_five, val_six, val_seven, val_eight, val_nine, val_ten)

Please round each number to the second decimal place.

| X = # of information 	| 1 	| 2 	| 3 	| 4 	| 5 	| 6 	| 7 	| 8 	| 9 	| 10 	|
|----------------------	|---	|---	|---	|---	|---	|---	|---	|---	|---	|----	|
| Probability          	| ? 	| ? 	| ? 	| ? 	| ? 	| ? 	| ? 	| ? 	| ? 	| ?  	|


```python
# Your answer here
```

## Question 5

Given that the person recalls at least 7 pieces of information, what is the probability that they recall all 10 pieces? Please round to the second decimal place, and assign your answer to the variable `question_5`.


```python
# Your answer here
```

## Question 6 - Confidence Intervals

A random sample of 35 Flatiron Students has a mean of 8.3 hours of sleep with a standard deviation of 3 hours.

In the cell below, calculate the sample's standard error and the z statistic for a 95% confidence interval. Assign your answer to the variable question_6 with a datatype of tuple and formatted as follows:

(standard_error, z_value)


```python
# Your code here
```

## Question 7 - Confidence Intervals

What is the 95% confidence interval for the mean number of hours slept by our sample of Flatiron Students?


```python
# Your answer here
```

## Question 8 - Select the matching distribution

Consider the following distributions


```python
# Run this cell unchanged
from visuals import multiple_choice
multiple_choice()
```


![png](index_files/index_18_0.png)


Please assign the visualization title letter to the prompt that best matches the data.

1. Normal, symmetrical, visual evidence of outliers.
1. Unimodel, skewed to the right, no apparent outliers.
1. Uniform, asymmetrical, no apparent outliers.
1. Normal, symmetrical, no apparrent outliers.
1. Bimodal, symmetrical, no apparent outliers.
1. Exponential, skewed to the left.
