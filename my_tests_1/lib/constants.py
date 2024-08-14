# Login page
#===============================================================================
LOGIN_PAGE_URL = "https://www.saucedemo.com/v1/"
ENTER_USERNAME_XPATH = "//input[@data-test='username']"
ENTER_PASSWORD = "//input[@data-test='password']"
CLICK_LOGIN = "//input[@value='LOGIN']"
ERROR_MESSAGE = "//h3[@data-test='error']"
#===============================================================================
# Inventory page
SC_BADGE = "//span[@class = 'fa-layers-counter shopping_cart_badge']"
SLL_0 = "item_0_title_link"
SLL_1 = "item_1_title_link"
SLL_2 = "item_2_title_link"
SLL_3 = "item_3_title_link"
SLL_4 = "item_4_title_link"
SLL_5 = "item_5_title_link"
#===============================================================================
# Procuct cards

SL_1 = "(//div[@class = 'inventory_item'])[1]"
SL_2 = "(//div[@class = 'inventory_item'])[2]"
SL_3 = "(//div[@class = 'inventory_item'])[3]"
SL_4 = "(//div[@class = 'inventory_item'])[4]"
SL_5 = "(//div[@class = 'inventory_item'])[5]"
SL_6 = "(//div[@class = 'inventory_item'])[6]"


#===============================================================================
# Product page
ADD_TO_CART_PDP = "//button[@class = 'btn_primary btn_inventory']"
REMOVE_PDP = "//button[@class = 'btn_secondary btn_inventory']"
BACK_BUTTON_PDP = "//button[@class = 'inventory_details_back_button']"

# Others
SIDE_BAR = "//div[@class = 'bm-menu']"
SORT_PRODUCT_CARDS = "//select[@class = 'product_sort_container']"
CART_BUTTON = "//div[@id = 'shopping_cart_container']"

# Cart page
#===============================================================================
CONTINUE_SHOPPING = "//a[@class = 'btn_secondary']"
CHECKOUT = "//a[@class = 'btn_action checkout_button']"