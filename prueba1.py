import requests
import json
import csv


def get_custom_attributes(data):
    
    # Obtener el valor de "custom_attributes" dentro de "allVariants" -> "attributesRaw"
    all_variants = data.get('allVariants', [])
    
    for variant in all_variants:
        attributes_raw = variant.get('attributesRaw', [])
        for attribute in attributes_raw:
            if attribute.get('name') == 'custom_attributes':
                valor = attribute.get('value')
                return valor
                break
        else:
            continue
        break
    else:
        return None
    
def extract_product_data(value):
    allergens_list = value.get("allergens", []).get("value")
    allergens = [item.get("name") for item in allergens_list if isinstance(item, dict)]
    sku = value.get("sku", []).get("value")
    vegan = value.get("vegan", []).get("value")
    kosher = value.get("kosher", []).get("value")
    organic = value.get("organic", []).get("value")
    vegetarian = value.get("vegetarian", []).get("value")
    gluten_free = value.get("gluten_free", []).get("value")
    lactose_free = value.get("lactose_free", []).get("value")
    package_quantity = value.get("package_quantity", []).get("value")
    Unit_size = value.get("Unit_size", [])
    net_weight = value.get("net_weight", []).get("value")
    
    if not Unit_size:
        print("Unit_size value is empty, changing to net_weight")
        Unit_size = net_weight
        
    data = {
        "allergens": allergens,
        "sku": sku,
        "vegan": vegan,
        "kosher": kosher,
        "organic": organic,
        "vegetarian": vegetarian,
        "gluten_free": gluten_free,
        "lactose_free": lactose_free,
        "package_quantity": package_quantity,
        "Unit_size": Unit_size,
        "net_weight": net_weight
    }  
    return data


def prueba_1():
    response = requests.get('https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json')

    if response.status_code == 200:
    
        data = response.json()    
        valor = get_custom_attributes(data)
        
        if valor is None:
            print("No se encontraron custom_attributes.")
            return False
        
        for key, value in valor.items():
        
            if key == "es-CR":
                value = json.loads(value)
                
                product = extract_product_data(value)
                print(product)
                
                with open('output_product.csv', mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=product.keys())
                    writer.writeheader()
                    writer.writerow(product)
                
                print("Datos del producto escritos en product_data.csv")
                return True
    else:
        print(f"Error: {response.status_code}")
        return False