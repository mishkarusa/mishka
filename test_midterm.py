from actions import driver_init, click_on_man, click_on_product_link, click_on_product_link, check_text, click_on_add_to_cart_link

def test_midterm():
    driver_init()
    click_on_man()
    click_on_product_link()
    click_on_add_to_cart_link()

    actual_text = check_text()
    expected_text = 'This is a required field.'

    assert expected_text in actual_text