from flask import Flask, request, Response
import ReceiptProcessorAPIHelper, ReceiptValidator
from werkzeug.exceptions import HTTPException, abort
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)
receiptIDMap = {}

@app.post("/receipts/process")
def processReceipts():
    errorResponse = Response("The receipt is invalid.", 400)
    receiptJson = request.get_json(silent=True)
    if receiptJson is None:
        abort(errorResponse)
    errors = ReceiptValidator.Receipt().validate(receiptJson)
    if errors:
        abort(errorResponse)
    id = ReceiptProcessorAPIHelper.generateIDasString()
    return {"id": id}

@app.get("/receipts/<string:id>/points")
def getReceiptPointsId(id):
    if receiptIDMap.get(id) is None:
        abort(Response("No receipt found for that ID.", 404))
    points = ReceiptProcessorAPIHelper.calculateReceiptPoints(receiptIDMap[id])
    return {"points": points}

