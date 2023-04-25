# Features
The system has the following features:
1. Verification of Source for Pre-Login Requests: The system can identify the source of requests to ensure they are coming from authorized sources.
2. Login and Registration APIs: Users can access the system using secure login and registration APIs.
3. Session Token Generation: Session token based authentication
4. CRUD Operations on Articles: Users can create, read, update, and delete articles securely.
5. Authenticated and Authorized Articles APIs: All article APIs, except for the "GET" API, are authenticated and authorized to ensure only authorized users can access and modify them.

## Project Setup 
Clone the repository
```
git clone https://github.com/shiva347/blogs.git
```

Create and activate a virtual environment
```
python -m venv myenv
```
For Windows 
```
myenv\Scripts\activate
```
For Linux or Mac
```
source myenv/bin/activate
```
Navigate backend project directory
``
cd backend
``
Install the required packages
```
pip install -r requirements.txt
```

```
python manage.py makemigrations users core articles 
```

```
python manage.py migrate
```
Create Superuser
``
python manage.py createsuperuser
``
Set the Source Key in the Authentication model(core), which will be used to validate whether the requests are coming from the right source or not
and in request header pass 'X-Source-Key'
```
X-Source-Key : <your_key>
```


```
python mange.py run server
```
