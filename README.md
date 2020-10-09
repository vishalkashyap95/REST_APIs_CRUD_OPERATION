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
<b>1 - Get all products.</b>
<pre>http://localhost:5000/api/v1/products</pre>
<b>2 - Get single product by ID.</b><br>
<pre>http://localhost:5000/api/v1/product/{product_id}</pre>
<pre>for eg : http://localhost:5000/api/v1/product/5f7ee7e40d74aa489e1ae1db
Sample output : 
[
    {
        "_id": "5f7ee7e40d74aa489e1ae1db",
        "brand_name": "oasis",
        "classification_l1": "women",
        "classification_l2": "women's shirts & tops",
        "classification_l3": "",
        "classification_l4": "",
        "currency": "GBP",
        "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/004263617?",
        "name": "Oasis Broderie Short Sleeve Top, Black",
        "offer_price_value": 15.0,
        "regular_price_value": 28.0
    }
]</pre>
<b>3 - Post/Insert into DB. Follow below steps to test it via Postman.</b><br>
<pre>a - Copy and Paste /insertProduct post URL in Postman and select method as "POST".
b - Set Headers "Content-Type" - "application/json"
c - Under Body tab > Click "raw" radio button > copy and paste below json into the body and select type as "JSON". Refer this link(![post_req_body](https://user-images.githubusercontent.com/46747690/95639350-c6775600-0ab5-11eb-95fe-56946bb9cfcf.PNG)).
       {
        "brand_name":"Louis Vuitton",
        "classification_l1":"Bag",
        "classification_l2":"",
        "classification_l3":"",
        "classification_l4":"",
        "currency":"GBP",
        "image_url":"https://lv.com",
        "name":"Bag",
        "offer_price_value":90,
        "regular_price_value":100
        }</pre> 

<pre>for eg : http://localhost:5000/api/v1/insertProduct
Sample output : 
{
    "message": "Successfully inserted with id :5f80ebbca7a9690529ff1196",
    "success": true
}</pre>

