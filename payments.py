"""Tiny payments module for the fixlock playground."""


def charge(customer, amount):
    return {"customer": customer, "amount": round(amount, 2), "status": "charged"}


def refund(customer, amount):
    return {"customer": customer, "amount": -round(amount, 2), "status": "refunded"}
