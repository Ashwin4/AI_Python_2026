# This is only study notes
"""
ML pipeline:
-----------
End to End work flow

what is ur business prblm?
Netflix churn prediction,
Credit card fraud or not
Bank can give loan or not

1.Data collection--gathering data for our businessprblm

--Diff sources we collet the data
--databses
--api
--sensors
--iot devices
--web data
--ERP,crm...
--cloud

2.Data preprocessing--


Cleaning and preparing the raw data for training
that means cleaning and transformatoin are happening,

--data cleaning--hadnling missig data duplicates,incorrect values
--DAta tranformation--
--1.Normalize the data--simply i can make my whole dataset into particualr
limits it can 0 to1 or -1 to 1
--2.Encoding the categorical variable
--3.Feature engineeering--createing new features 

3.EDA--Exploratory Data Analysis
--Understanding the patterns,relationships in our dataset

simply some stats
visualizations

4.Model building/trainng

---here we select the algorithms and fit them to training data

--->split data set--training,testing,validation
--->select the alogorthm--based on data type and businees problm requirement
        --Regression
        --classifcation
        --Clustering

--->Train the model-->After trainng we get some predictions then we have to compare this with my actuals..
--->Testing the model

5.Model Evaluation

Measuring how well our model performs

choose the metrics based on the type of the prblm

Regression---MAE,RMSE,Rsquare

Classification--Accuracy,Precision,Recall,F1 score,ROC-AuC

clustering---Silhouette score--


6.Model deployment

Make the trained model available for real time or batch predictions--

7.Model Monitoring

After deployment how the model performs checking

--Data drift-->real word data keep on changes simply the model performs degrades over the time

finally we might need to retrain the model on fresh data


###########################################################################################

ML Terminology:
--------------

Features and labels:
-------------------
Features(X)--input variables--Independent variables
Label(y)--Output variable--dependent variable--Target variable

Observations/Samples:
---------------------
EAch row in our dataset is one sample or observation
EAch column--one feature apart from that target column

Target variable:
----------------
this is what we have to predict


Model
-----

A matmematical function that maps input(X) to output(y)

After training that algorithm that we used on top of the data.

Error:
------
Diff between actual output and predicted output it tells how wrong our predictions are

why we need calculate error?

-->To check how accurately my algorithm works

minimize the error between predicions and actuals.


How to measure the error:
------------------------
Model evaluation measureing the error only


Training:
---------
The process of learning from data, but here we adjust weights to reduce the errors

Weights?--

I want to make cake--flour,sugar,eggs,....

how much flour,sugar,eggs---yummy cake


Simply weight tells how imp each input feature is when making some predctions


Ex: predicitng house price:

Size---here size sqfeet it is matters--here the weight is more size
wall color--not that much--here very less weight









-->Here the model learns automatically which feature are more or less useful

-->how does the models learns the weights?

--During trainng the model starts with random weights

--It predicts the outputs

--It compares the prediction and actuals output using error meassure(loss function)

--It adjusts the weights to reduce the error

This adjustment will happens through Optimization algorithms

Gradient DEscent

SGD--Stochastic Gradient Descent

Adam Optimizer



Prediction:
----------
Using the training model to make predictions on new unseen data

Loss fucntion/cost function:
----------------------------
It measures how wrong the model is

MSE,cross entropy....

Overfitting:
============

the model learns the traingn data very well 

how to know ?

high accuracy on trainng data--90

Low accuracy on test data--?50


Underfitting:
-----------

the model is very simple it cannot captures the patterns in the data

how to know?

low accuracy on trainng data--50

low accuracy on testing data--40


Hyperparameters:
----------------

what is parameters?

that will learned automatically by the model from the data

Hyperparameters:
-----------------
Choosen manually before training to control the how the learning happens

why we need this?

simply they affect the model accuracy,and process of the model

If we did not taken those model might underfit or overfit

so its better to take hyperparemeter tuning for better learning and performance




Cross validation
-----------------
we know that our models can do underfit or overfit

what we need is a fair way to estimate how well our model generalizes

Cross validation a method or technique to test the model by trainng and testing it multiple times on diff 
parts of data

80% training--noisy data
20% testing--clean

here the accuracy of test data it might depend upon 


split the data into diff parts K--say it can be 3,4,5,...10

Train the model diff parts

each time we use  a diff validation set and remainng part as trainng

compute thar performnace at each part

Average them all

K=5 parts

Fold/Part               Train data              validation/test
1                       2 ,3,4,5  --80%              1----50%
2                       1,2,3,4      --90            5---40%
3                       1,3,4,5                      2
4                       1,2,4,5                      3
5                       1,2,3,5                      4


average accuracy=Mean of all 5 validation accuracies

more reliable accuracy---useing mulitiple train/test combinations

here it might detect the overfitting early stage




Bias and variance
------------------

every ML models makes some prediction error

we can consider those errors in to 3 parts

1.Bias--it is because worng assumptions--model is too simple

it assumens a wrong relationship--may be that is curved data but my model assumption as liner


It performs poorly on training and testing data--underfitting


2.Variance:
-----------

here it performs well on traing data but fails on new data

overfitting

variance  more


how to balances this
--------------------

simply minimising the error--lowest error


bias            varinace                Result
low             high                    overfitting
high            low                     underfitting
moderate        moderate                good fit/perfect model






3.irreducible error---noise in data the model cannot fix


#############################################################################################3

1.Relationship between input and output is looks like a straight line


Ex:sales vs marketing

More ads--->More sales

Student study more-->Score more


2.Features are independent

Simply inputs do not strongly influence each other

Ex:
---
sqfeet  wall color location 

Ex:
---
dependent feature

If two features are related--linear regression gets confused

Discount_percentage     Amount
----------------------------------


3.Data is not too noisy

noisy:
------

data with random errors,flucations,disturbances,incorrect,missong or wrong,completely abnormal some rows.....


Ex:
---
Uber Taxi
---------
Uber Fare prediction

Distnace increases fare increase-->staringht line realtionship

some situations:
----------------

Fares unusually high--Driver took the long route
FAres highe even for short distance---Traffic is heavy
Fares unusally low--May be the user got discount
Distnace wrongly calculated--GPS prblms
..........


if noisy is more---linear regression poorly will perform


How to check noisy?

simply try to clean the data

plot it in that time may be data more scattered not a straight line

Lets imagine curved kind of data plot

then go for Polynomial regression

if the data set is very small and it has very less feature 

i have to take 15 degrees i have more features---Polynomial

Alternative--DTR,RFR




"""