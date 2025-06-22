from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

def get_pokedata_price(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    time.sleep(5)

    try:
        price_element = driver.find_element(By.CLASS_NAME, "MuiTypography-avenir_24_700")
        price = price_element.text.strip().replace("$", "")
    except Exception:
        price = None

    driver.quit()
    return price

@app.route('/price', methods=['GET'])
def price():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL manquante'}), 400

    price = get_pokedata_price(url)
    if price is None:
        return jsonify({'error': 'Prix non trouvé'}), 404
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
