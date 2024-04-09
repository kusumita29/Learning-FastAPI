from typing import Annotated, List, Optional
from fastapi import APIRouter, Header
from fastapi.responses import HTMLResponse, PlainTextResponse, Response

products = ["camera", "book", "magazine"]

router = APIRouter(prefix="/product", tags=["product"])


@router.get("/all")
def get_all_products():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.get(
    "/{id}",
    responses={
        200: {"content": {"text/html": {"example": "<div>Product</div>"}}},
        404: {"content": {"text/plain": {"example": "Product not found"}}},
    },
)
def get_product(id: int):
    if id > len(products):
        return PlainTextResponse(
            status_code=404, content="Product not available", media_type="text/plain"
        )
    else:
        output = f"""
            <head>
            <style>
                .product{{
                height: 20px;
                width: 150px;
                border: 5px green;
                background-color: lightblue;
                text-align: center;
                }}

            </style>
            </head>
            <body>
            <div class = 'product'> {products[id-1]} </div>
            </body>
        """
        return HTMLResponse(content=output, media_type="text/html")
