### README- Local Django API Environment Setup

----

#### 1. Installation Steps- UBUNTU
1. sudo apt-get update
2. **Python 3.6.x**	
	- sudo apt-get install python3.6
3. **pip3**
	- sudo apt-get -y install python3-pip
4. **installing all the modules**
	- pip3 install -r requirements.txt

----

#### 2. Installation Steps- WINDOWS 
1. **Python 3.6.x**
	- https://www.python.org/ftp/python/3.6.7/python-3.6.7.exe
	- Make sure to add pip to path when you install.

2. **pip** *(Optional)*
	- https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command

3. **installing all the modules**
	- pip install -r requirements.txt

----

#### 3. Check Installation- UBUNTU & WINDOWS
- pip3 freeze / pip freeze

----

#### 4. Steps: Starting Django Server (UBUNTU)
1. Open Terminal in the directory which contains your **apps / manage.py** file. 
2. Run- **python3 manage.py makemigrations** 
   *(to be runned once in your system, not to be runned everytime you run server)*
3. Run- **python3 manage.py migrate** 
   *(to be runned once in your system, not to be runned everytime you run server)*
4. Run- **python3 manage.py runserver** 
   *(to be excuted everytime you run server)*

----

#### 5. Steps: Starting Django Server (WINDOWS)
1. Open Command Prompt in the directory which contains your **apps / manage.py** file. 
2. Run- **python manage.py makemigrations** 
   *(to be runned once in your system, not to be runned everytime you run server)*
3. Run- **python manage.py migrate** 
   *(to be runned once in your system, not to be runned everytime you run server)*
4. Run- **python manage.py runserver** 
   *(to be excuted everytime you run server)*

----

#### 6. Steps: Running Django API (UBUNTU & WINDOWS)
1. Follow the Readme of the API you want to run.
2. Click on the API Endpoints via Web Browser or Postman

----

#### AUTHOR-
- **AAYUSH GADIA** 
- **contact info: gadia.aayush@gmail.com**
