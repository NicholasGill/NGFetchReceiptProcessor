from flask import Response

class invalidReceiptError(Response):
    def __init__(self):
        super().__init__("The receipt is invalid.", 400)

class notFoundReceiptError(Response):
    def __init__(self):
        super().__init__("No receipt found for that ID.", 404)
