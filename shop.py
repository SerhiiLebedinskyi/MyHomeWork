from pywebio.input import input as pw_input
from pywebio.input import slider, NUMBER
from pywebio.output import put_html, put_success
from decimal import Decimal, ROUND_HALF_UP
import decimal
import logging


# CONSTANTS
APPLE_PRICE = Decimal("52.75")
BANANA_PRICE = Decimal("81.40")

# LOG SECTION
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s -%(message)s",
    handlers=[logging.FileHandler("shop.log"), logging.StreamHandler()],
)

# HEADER
put_html("<h1>Welcome to our Fruit Shop<h1>")

# INPUT SECTION
apples_waight = slider(
    "Apples", type=float, min_value=0, max_value=5, value=0.01, required=True
)

bananas_waight = pw_input("Bananas", type=NUMBER, required=True, min=0, max=10, value=1)

# ROUNDED SECTION
apples_waight = Decimal(apples_waight).quantize(Decimal("0.000"), ROUND_HALF_UP)

bananas_waight = Decimal(bananas_waight).quantize(Decimal("0.000"), ROUND_HALF_UP)

# COUNT SECTION
apples_cost = (apples_waight * APPLE_PRICE).quantize(Decimal("0.00"), ROUND_HALF_UP)
bananas_cost = (bananas_waight * BANANA_PRICE).quantize(Decimal("0.00"), ROUND_HALF_UP)
total_cost = apples_cost + bananas_cost

# OUTPUT SECTION
put_success(
    f"Total cost: \n apples_cost \t {apples_cost} \n banans_cost \t {bananas_cost} \n total_cost \t {total_cost}"
)
