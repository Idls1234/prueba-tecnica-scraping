from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from prueba2 import get_products
from prueba1 import prueba_1
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/prueba1")
async def get_articles():
    if prueba_1():
        file_path = "output_product.csv"
        if os.path.exists(file_path):
            return FileResponse(path=file_path, filename="output_product.csv", media_type='text/csv')
        else:
            return {"error": "File not found"}
    else:
        return {"error": "No se encontraron custom_attributes."}

@app.post("/prueba2")
async def extract_products(url: str):
    found_products = get_products(url)
    return {"url": url, 
            "products": found_products}