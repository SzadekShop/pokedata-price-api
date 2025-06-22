from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_pokedata_price(url):
    options = Options()
    options.add_argument("--headless")  # mode sans fenêtre visible
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    time.sleep(5)  # attend que la page charge bien

    try:
        price_element = driver.find_element(By.CLASS_NAME, "MuiTypography-avenir_24_700")
        price = price_element.text.strip().replace("$", "")
    except Exception:
        price = "Prix non trouvé"

    driver.quit()
    return price

if __name__ == "__main__":
    url = "https://www.pokedata.io/product/Ruler+of+the+Black+Flame+Booster+Box"
    print("Prix :", get_pokedata_price(url))