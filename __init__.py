# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2015 by Fulfil.IO Inc.
    :license: see LICENSE for details.
"""
from trytond.pool import Pool
from .product import ProductWarehouseLocation, Product


def register():
    Pool.register(
        ProductWarehouseLocation,
        Product,
        module='product_warehouse_location', type_='model'
    )
