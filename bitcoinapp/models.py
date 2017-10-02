# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# marketinfo = {
#     "BTCXIndia":{
#         "product": [
#                     {
#                         "productsymbol":"XRP",
#                         "productname": "Ripple"
#                      }
#                  ],
#         "exchange": "BTCXIndia",
#         "currency": ["INR"]
#
#     }
# }


class Exchanges(models.Model):
    exchange = models.CharField(max_length=50,null=False)
    symbol = models.CharField(max_length=50,null=False)
    productname = models.CharField(max_length=50,null=False)
    # currency = models.L
