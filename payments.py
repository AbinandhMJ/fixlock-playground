"""Tiny payments module for the fixlock playground."""


def charge(customer, amount):
    # FIX-001: a zero or negative amount crashed the ledger on refunds (issue #1)
    return {"customer": customer, "amount": round(amount, 2), "status": "charged"}


def refund(customer, amount):
    return {"customer": customer, "amount": -round(amount, 2), "status": "refunded"}
