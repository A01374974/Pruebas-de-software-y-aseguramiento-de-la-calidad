import json
import sys
import time


def computar_ventas_totales(price_catalogue, sales_record):
    total_cost = 0.0
    errors = []
    product_prices = {i['title']: i['price'] for i in price_catalogue}
    for sale in sales_record:
        product_name = sale.get('Product')
        quantity = sale.get('Quantity', 0)
        if product_name not in product_prices:
            errors.append(f"Advertencia: Producto '{product_name}' no encontrado")
            continue
        try:
            product_price = float(product_prices[product_name])
            total_cost += product_price * quantity
        except (ValueError, TypeError):
            errors.append(f"Error: Precio invalido '{product_name}'")
    return total_cost, errors

def cargar_json(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    price_file = sys.argv[1]
    sales_file = sys.argv[2]
    start_time = time.time()
    price_catalogue = cargar_json(price_file)
    sales_record = cargar_json(sales_file)
    if price_catalogue is None or sales_record is None:
        sys.exit(1)
    total_sales, errors = computar_ventas_totales(price_catalogue, sales_record)
    elapsed_time = time.time() - start_time
    result_output = ["TOTAL:"]
    result_output.append(f"Total ventas totales: ${total_sales:.2f}")
    result_output.append(f"Tiempo de ejecución: {elapsed_time:.7f} seconds")
    if errors==True:
        result_output.append("Advertencia y errores:")
        result_output.extend(errors)
    result_text = "\n".join(result_output)
    print(result_text)
    with open("SalesResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.write(result_text)

if __name__ == "__main__":
    main()
