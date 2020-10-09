# REST APIs, Created in flask for CRUD operations
  1 - Hosted given data for this task on MongoDB Atlas<br>
  2 - Created APIs for performing CRUD operations<br>
  3 - Dockerized entire application, and can be deployed locally with "Docker run" command.
  
<h1># Get Started</h1>
<h2>Installation : There are 2 ways to install and run this project</h2>
<h4>1 - Install and run with Docker<h4>
<pre>docker run -it -p 5000:5000 vishalkashyap95/rest_apis_flask:v1</pre>
<h3>OR</h3>
<h4>2 - Install and run from source<h4>
<pre>
git clone https://github.com/vishalkashyap95/REST_APIs_CRUD_OPERATION.git
cd REST_APIs_CRUD_OPERATION
pip install -r requirements.txt
python app.py
</pre>
<h1>Usage</h1>
There are total 5 APIs. Follow below step to call/test locally.<br>
<b>1 - Get all products. Return all the products from the DB.</b>
<pre>http://localhost:5000/api/v1/products</pre>
2 - Post/Insert into DB. Follow below steps to test it via Postman.<br>
    <pre>a - Copy and Paste below post URL in Postman and select method as "POST".<br>
    b - Set Headers "Content-Type" - "application/json"
    c - Body</pre> 
<pre>http://localhost:5000/api/v1/insertProduct</pre>
