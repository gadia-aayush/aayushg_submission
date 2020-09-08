#### README- Assignment Submission :: Aayush Gadia

-----

##### API Name, Description, it's EndPoints, TestCases with Snaps-
1. **survey**

- *API EndPoints-*
	- *Getting Survey Qns URL- http://127.0.0.1:8000/survey/?id=1 (GET API)*


- *Description-*
	- *Here, only the survey id has to be passed in the **id**variable in the **API Endpoints** shown above. **Every API Call, would return ONE question & it's options (prepared from the file shared- survey.yaml), which are mapped to that particular survey id.***<br><br>
	- ***Every call on API Endpoint would keep returning the question & it's option until all the questions of that particular survey id is covered.***<br><br>
	- ***Also, here the ORDER in which the questions come in the survey are not a constrain (as per the doc shared), therefore the questions are randomized and they are not following any order, like after this questions, that will come and like that.***<br><br>
	- *Below are the snaps-<br>*
		- ![id=1.0](https://github.com/gadia-aayush/rough/blob/master/id=1.0.png) | ![id=1.1](https://github.com/gadia-aayush/rough/blob/master/id=1.1.png)
		- ![id=1.2](https://github.com/gadia-aayush/rough/blob/master/id=1.2.png) | ![id=1.3](https://github.com/gadia-aayush/rough/blob/master/id=1.3.png)
		- ![id=1.4](https://github.com/gadia-aayush/rough/blob/master/id=1.4.png)<br><br>

	- *For the example above, their are 4 questions mapped to survey id = 1.*


- *Test Cases-*
	- *Error Handling has been implemented very properly & all the corner test cases has been covered, making sure that the API never breaks.*<br><br>
	- ***Some of the URL's** of corner test cases are-*
		- http://127.0.0.1:8000/survey/?
		- http://127.0.0.1:8000/survey/?id=aayush
		- http://127.0.0.1:8000/survey/?id=4
		- http://127.0.0.1:8000/survey/?id=423
		- http://127.0.0.1:8000/survey/?id=2 <br><br>
	- *Below are the snaps-<br>*
		- ![t1](https://github.com/gadia-aayush/rough/blob/master/t1.png) | ![t2](https://github.com/gadia-aayush/rough/blob/master/t2.png)
		- ![t3](https://github.com/gadia-aayush/rough/blob/master/t3.png) | ![t4](https://github.com/gadia-aayush/rough/blob/master/t4.png)
		- ![t5](https://github.com/gadia-aayush/rough/blob/master/t5.png)

-----

##### DATABASE-

- *Here, **the default SQLite Database is used for the Django Application.***
- *Models that were created were are- **Survey, Question, Qptions, Relation_Survey_Qn, Relation_Question_Opn***
- ***Survey model** stores information like- survey id, description, start & end date, active status*
- ***Question model** stores information like- question id & question text.*
- ***Options model** stores information like- option id & option texts.*
- ***Relation_Survey_Qn** stores information like relationship id, last visited status, question id (Foreign Key), survey id (Foreign Key).*
- ***Relation_Question_Opn** stores information like relationship id, option id (Foreign Key), question id (Foreign Key)* 
- *To, know more please visit the **db.sqlite3.***

- *Screenshots-*
	- ![db-1](https://github.com/gadia-aayush/rough/blob/master/db-1.png)
	- ![db-2](https://github.com/gadia-aayush/rough/blob/master/db-2.png)
	- ![db-3](https://github.com/gadia-aayush/rough/blob/master/db-3.png)
	- ![db-4](https://github.com/gadia-aayush/rough/blob/master/db-4.png)
	- ![db-5](https://github.com/gadia-aayush/rough/blob/master/db-5.png)
	
-----

##### Requirements-

- **Available in the Repo.**[ **Click Here**](https://github.com/gadia-aayush/aayushg_submission/blob/master/requirements.txt)

-----

##### Author-
- **AAYUSH GADIA**
- **Phone- +91- 8334827095  |  Email- gadia.aayush@gmail.com**
- **[Wesbite](https://gadia-aayush.github.io/) | [GitHub](https://github.com/gadia-aayush)  |  [LinkedIn](https://www.linkedin.com/in/gadia-aayush/)**

------
