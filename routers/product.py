from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(
    prefix="/product",
    tags=["product"]
)

products = ["watch", "phone", "laptop"]

@router.get("/")
async def get_products():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")
