import time
import common.apitest
import pagemodules.planspage
import pagemodules.cartpage
import common.comm


def test_1():
    common_handler = common.comm.comman_class()
    data_handler = common_handler.getTestData("Test1")  # test data file access

    driver = common_handler.invoke_driver(data_handler["ui_url"])  # driver initialization
    get_obj = common.apitest.api_get()
    plans_obj = pagemodules.planspage.get_element(driver)

    log = common_handler.getLogger()  # logger init

    log.info("Description : Validate all plans cta ('Add to cart' button) in the UI matches with the API's ctaLabel "
             "field (under planListing/plans/)")

    # executes get request for api's
    (labelstr, labelcnt) = get_obj.get_test1(data_handler["api_url"],data_handler["api_label"])

    log.info(f'Total number of label in api request : {labelcnt}')
    log.info(f'Text for each label in api request: {labelstr}')

    # Get plans cta for all the buttons on UI
    (plans_str, plans_cnt) = plans_obj.get_multi_text(data_handler["plan_parent_path"], data_handler["plan_child_path"])

    log.info(f'Total number of label in UI : {plans_cnt}')
    log.info(f'Text for each label in UI: {plans_str}')

    # validates the ctalabel on UI and from API's are matching
    assert plans_str == labelstr and labelcnt == plans_cnt, log.critical(
        "The total number of cta button or its labels on UI and API are not matching : FAIL \n")
    log.info("The total number of cta button and its labels on UI and API are matching : PASS \n ")

    common_handler.close_driver(driver)


def test_2():
    common_handler = common.comm.comman_class()
    data_handler = common_handler.getTestData("Test2")  # test data file access

    driver = common_handler.invoke_driver(data_handler["ui_url"])  # driver initialization
    plans_obj = pagemodules.planspage.get_element(driver)
    cart_obj = pagemodules.cartpage.sticky_display(driver)

    log = common_handler.getLogger()  # logger init

    log.info(f'Select any plan and validate if the price shown in sticky cart is same as the plan selected')

    # get the selected plan price
    plan_price = plans_obj.get_ele_text(data_handler['plan_parent_path'], data_handler['plan_child_path'])
    price_p = plan_price.split("\n")

    # Click on selected plan to Add to cart
    plans_obj.get_ele_click(data_handler['plan_button_parent'], data_handler['plan_button_child'])
    log.info(f'Selected plan details : {price_p[0]} {price_p[1]}')

    # get the selected plan price from the sticky cart
    price_s = cart_obj.get_sticky_cart_text(data_handler['sticky_parent_path'], data_handler['sticky_child_path'])
    log.info(f'Plan details displayed on sticky cart : {price_s}')

    # Validates the price of selected plan and price on sticky cart is matching
    assert price_p[0] in price_s and price_p[1] in price_s, log.critical(
        "The plan selected and displayed on sticky cart is not matching : FAIL \n")
    log.info("The plan selected and displayed on sticky cart is matching : PASS \n ")

    common_handler.close_driver(driver)


def test_3():
    common_handler = common.comm.comman_class()
    data_handler = common_handler.getTestData("Test3")  # test data file access

    driver = common_handler.invoke_driver(data_handler["ui_url"])  # driver initialization
    plans_obj = pagemodules.planspage.get_element(driver)
    cart_obj = pagemodules.cartpage.sticky_display(driver)

    log = common_handler.getLogger()  # logger init

    log.info(f'Proceed to cart and validate if cart page is shown with the correct product')

    # Click on selected plan to Add to cart
    status = plans_obj.get_ele_click(data_handler['plan_button_parent'], data_handler['plan_button_child'])

    # get the selected plan price from the sticky cart
    price_s = cart_obj.get_sticky_cart_text(data_handler['sticky_parent_path'], data_handler['sticky_child_path'])
    log.info(f'Plan details displayed on sticky cart : {price_s}')

    time.sleep(10)

    # Click on "continue to cart" button on sticky cart
    status1 = cart_obj.get_sticky_button_click(data_handler['sticky_button_parent'], data_handler['sticky_button_child'])

    # get the selected plan price from the cart page
    price_c = cart_obj.get_sticky_cart_text(data_handler['cart_parent_path'], data_handler['cart_child_path'])
    price_c = price_c.split("\n")

    log.info(f'Plan detail displayed on checkout page {price_c[0]} {price_c[1]}')
    log.info(f'Plan detail displayed on checkout page {price_s}')

    # Validates the price of selected plan and price of selected item on cart page is matching
    assert price_c[0] in price_s and price_c[1] in price_s, log.critical("Plan on sticky cart and checkout page is not matching : FAIL \n")
    log.info("Plan on sticky cart and checkout page is matching : PASS \n ")

    common_handler.close_driver(driver)
