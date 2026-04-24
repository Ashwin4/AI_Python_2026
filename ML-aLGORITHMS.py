# This is study and some codings
"""
-----------------
Machine learning:
------------------

Netflix
amazon
google gmail
Youtube 
siri
alexa

ML is subset of AI

ML:teaching machines to learn from data.

Data means any kind of data it can strucuterd,unstructred,semistrucuterd

Structres:tables,excel,....

Semi strucutres:json files,tag related files,....
{id:101,name:ak  }

<id>101</id>
<name>ak</name>
........

Unstrucuter:
-----------

Images,videos,Audios,TExt data.....

I will give some photos of cats and dogs-->can it learn?--yes learn-->

You will send new cat image/dog image--it will correctly predict it.

#############################################################################

Types of ML:
------------

1.Supervised learning:
-----------------------
data has labels

We teach the machines using labeled data---means we already know the correct answers for the inputs

To predict for new data i am doing trainng.

Email:
-------

-->Input as email
-->Output as spam/not

Algorithms in SL:
----------------

Two types

1.Regression---output is numerical

Ex:
Predicting house price

sqft        no of rooms      location      price
1000        3                   prime       
2000        2                   outskirts   
....        ,,                  ...         ...

.....       ...                 .....       ....



->stock prices

->temperature predictions

->predict sales amount
#########################################################33

Algorithms:
-----------

Linear regression:
-------------------

--simple lienar ---one input feature
--multiple linear --more than one input feature

-Relationship between input and output alomist straight line
-Features are independent
-Here the data is not too noisy-->

Meainng noisy means-->errors,fluctuations,outliers,abnormal kind of data

Ex:Creditcard transcation

Predict the future the spending price

Noisy :
-------
One time huge purchase
wrong swipes or errors
amount spending wrong amount


Sensor data:
-------------
Collecting from machinery the noise data
--missing readings
--wrong amplitude
--wrong temp

.....

Uber taxi:
----------

We want predict uber fare using distance?

noise in the data:

Driver takes long route--fare unusually high
traffic heavy --fare will increase
gps singled losed--distance wrongly calculated
.....


#############################################################################################################

Linear regression tries to draw stringh line through the points if points are too scatterd then line becomes
meaningless.

Random forest,Deciosn tree can handle noise better

How to identify the noise?
---------------------------
Ploting after cleaning the data

########################################################################################################


Multiple liner regression
--------------------------

Here Mulitple input features influence the output

Same as linear regression

#######################################################################################################

Polynomial regression
-----------------------

here we use this the relationship is curved that means non linear

-->weather forcasting in diff seasonaal patterns

-->Electricity kind of data

-->Plane example 

############################################################################################3

1.First indetify the problem

2.REgression--output is numneric
  classification--output categorical

3.Data size:
----------
Small--

Medium--

Large--

4.linear/non linear data
----------------------


5.Check features:
--------------

Images---SVM/DL
TExt--naive bayes
numerical kind of data--
some other features:


6.Depending business need we have 

First al:Highest accuracy-slow


Second Alg:Very speed-- accuracy is very close 1


#############################################################
Decciosn tree regressor

Random forest RRegressor

##############################################################
....
2.Classifcation---output is categorical

Email---TExt passing ---live data we cannt we get in chatgpt?

Predicting customer churn---is the cusotmer will stay on top of this platform or he will leave
Netflix/amazon prime/youtube/network connection/.....

?

Churn prediction?--will the customer will stay or not?

NEtflix :
------------------

what kind of data?
------------------

DAta collection:
=------------------
user activity--->how many hours watched per week/day 
            ---->no of times user login
            ---->he might skipped video,liked video

subscription data--->plan types,price,renewel date(billind date)

User intrests---what genres watched,ratings

complints issues

Age--18 20 21


here our output variable is churn/not

we got it as churn==>apply some special offers


..................................

data cleainng and preprocessing---

Feature enginerring---creating some new features--

which grps      wht kind of genres they watching

18 to 24            Action

25 to 30            Adventures

#####################################33

Train and test
---------------
divind the data into 80 20 percent like thht

model trainng
----------------
diff ml algorithms--


model evalution:
--------------
Messaure the accuracy


Deplyoment
------------
USe the best model to predict the churn for new customers in real time

#################################################################################33

--->bank to give loan to customer---input........output:loan/not

cusotmer--persnl info,how many years bak acc,how many acc ,credit score,taken any loans,how much 
taken,CC,.....employ,buisness,self emplyed--->

--->Face recongnitation-----input...features of face--->Output:is that u or not


##################################################################################

Algorthsm in classification:
----------------------------

Logistic regression

Decsoin tress classfier

Random forest classfier

Support machine

NAive bayes

####################################################################################



2.Unsupervised LEarning:
-----------------------
there are no predefined outputs here the machines can find the patterns,strucure or relationships in the data
on its own.

Ex:Youtube
----------

user1
user2
user3

.....
simply collect the data

wht kind of data:
----------------
wht user seeing
wht he skipping
whe he is liking 
wht is commeting
sharing
......

....
how much time spending on type video
......
After collecting this data they apply alogorthm on  top of that 
They will categorize them diff grps/clusters
cluster1--Tech---only tech i will give some recommedations
cluster2--Food---food related i will recomenatoins
cluster3--Travel vlogs
.....

....

ALgorithm:
----------

K means algorithm
Gaussion
hirehcical algorthan
Dbscan



3.Reinforcement LEarning
------------------------

It is a type of ML.

Here the agents learns by doing some actions and getting rewards or penalties.

Components in RL:
-----------------


Agent---The learner-----Self driving cars----- 

Environment--everything that agent can interacts with-->the road,traffic,signals,diff objects....

What kind of actions:turn left,turn right,accelerate,start,stop......

The position of current state of agent--

Reward:Feedback after each action---car hitted another car backside---ve feedback


############################################################################################33
Gaming
self drinvg cars
Robotic
Health care--


Environment--patient health condtion
Action:given medication A,changed the dose to B,started/stopped some antiboitic,decrese the sugar levels

Reward--patiet recovery






-----------
Algorthms:
-----------

Q-learning
Deep Q network 
Reinforce
A3C
....


"""