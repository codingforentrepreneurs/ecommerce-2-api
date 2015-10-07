## eCommerce 2 API Walkthrough
An introduction to the eCommerce 2 API course.



#### 1. Clone/Download the REPO

[Download archive](https://github.com/codingforentrepreneurs/ecommerce-2-api/archive/master.zip)

Clone with Git
```
mkdir ecommerce-2-api-master && cd ecommerce-2-api-master
git clone https://github.com/codingforentrepreneurs/ecommerce-2-api.git .

```


#### 2. Create & Activate Virtualenv 
Assuming you are in the `ecommerce-2-api-master` directory created above

```
virtualenv .
```


Activate Virtual Environment

Mac/Linux: ```source bin/activate```

Windows: ```.\Scripts\activate```


#### 3. Install Requirements

```
(ecommerce-2-api-master)$ cd src
(ecommerce-2-api-master)$ pip install -r requirements.txt

```



#### 4. Run Local Server

```
(ecommerce-2-api-master)$ python manage.py runserver 

```


#### 5. Open API url:

[API URL @ http://127.0.0.1:8000/api/](http://http://127.0.0.1:8000/api/)


#### 5. Run API Tests:

Open new Terminal/Command Prompt and keep the above server running
```
cd /path/to/your/ecommerce-2-api-master
```

Activate Virtual Environment

Mac/Linux: ```source bin/activate```

Windows: ```.\Scripts\activate```


```
(ecommerce-2-api-master)$ cd src/ecommerce2
(ecommerce-2-api-master)$ python api_tests.py

{"order_token":"eydvcmRlcl9pZCc6IDU4LCAndXNlcl9jaGVja291dF9pZCc6IDExfQ=="}
```








