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

Install the required packages
```
pip install -r requirements.txt
```

```
python mange.py makemigrations
```

```
python mange.py migrate
```
## Set the Source Key in the Authentication model, which will be used to validate whether the requests are coming from the right source or not

```
python mange.py run server
```
