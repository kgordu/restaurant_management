from .constants import MENU_ITEMS, TABLES, CUSTOMER_ORDERS, CUSTOMER_BUDGET
from .restaurant import Restaurant
import logging

logging.basicConfig(
  level=logging.INFO,
  filename='src.log',
  filemode='a',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Package is initialized")


__version__ = "1.0.0"
__date__ = "22-06-2024"
__email__ = "kivancgordu@hotmail.com"
__status__ = "production"

__all__ = ['Restaurant', 'MENU_ITEMS', 'TABLES', 'CUSTOMER_ORDERS', 'CUSTOMER_BUDGET']
