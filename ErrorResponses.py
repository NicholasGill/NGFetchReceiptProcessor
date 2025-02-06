from flask import Response

def invalidReceiptErr(errorMessage: str):
    return Response(errorMessage, 400)

def notFoundReceiptErr(errorMessage: str):
    return Response(errorMessage, 404)