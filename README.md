<h1>Nicholas Gill Fetch Take Home</h1>

<h2>Implementation of the Fetch Receipt Processor Take Home.</h2> 
My implementation contains two endpoints, 

    Path: /receipts/process
    Method: POST
    Payload: Receipt JSON
    Response: JSON containing an id for the receipt.


    Path: /receipts/{id}/points
    Method: GET
    Response: A JSON object containing the number of points awarded.


<h3>Steps for running code.</h3>
<ol>
    <li>Clone the repo</li>
    <li>cd into the project directory</li>
    <li>run <code>sudo docker compose up --build</code>.</li>
</ol>

The endpoints should be available at http://localhost:8080.

If you want to run tests, 
<ol>
    <li> pip install -r requirements.txt</li>
    <li> run `pytest` in the same directory</li>
</ol>
<h2>Example Curl Commands to Test Endpoints</h2>
<p>
Process Receipt Endpoint:
    <code>
    curl --location 'http://localhost:8080/receipts/process' \
    --header 'Content-Type: application/json' \
    --data '{
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {
        "shortDescription": "Mountain Dew 12PK",
        "price": "6.49"
        },{
        "shortDescription": "Emils Cheese Pizza",
        "price": "12.25"
        },{
        "shortDescription": "Knorr Creamy Chicken",
        "price": "1.26"
        },{
        "shortDescription": "Doritos Nacho Cheese",
        "price": "3.35"
        },{
        "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
        "price": "12.00"
        }
    ],
    "total": "35.35"
    }'
    </code>
</p>
Example Output: <code>{"id":7ca24990-de7e-4233-adbf-5fc6ab421731}</code>


Get Points Endpoint:
    <code>curl --location 'http://localhost:8080/receipts/7ca24990-de7e-4233-adbf-5fc6ab421731/points'</code>

Example Output: <code>{"Points": 28}</code>