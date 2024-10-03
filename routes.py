from flask import Flask, request, jsonify, send_file
import os
import asyncio
from prueba1 import prueba_1
from prueba2 import get_products_playwright 

app = Flask(__name__)

@app.route('/prueba1', methods=['GET'])
def get_articles():
    # Simula la función prueba_1()

    if prueba_1():
        file_path = "output_product.csv"
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True, download_name="output_product.csv", mimetype='text/csv')
        else:
           return jsonify({"error": "File not found"}), 404
    else:
        return jsonify({"error": "No se encontraron custom_attributes."}), 404

@app.route('/prueba2', methods=['POST'])
def extract_products():
    data = request.get_json()
    url = data.get('url')
    print("URL: " + url)
    
    # Ejecutar la coroutine y obtener el resultado
    found_products = asyncio.run(get_products_playwright(url))
    return jsonify({"url": url, "products": found_products})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)