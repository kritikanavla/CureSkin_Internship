from behave import given, when, then

@given("Open cureskin main page")
def open_cureskin(context):
    context.app.main_page.open_main_page()


@when("Click on 'Shop by category'")
def click_shop_by_category(context):
    context.app.header.click_shop_by_category()


@when("Click on Body")
def click_body(context):
    context.app.header.click_body()


@then("Verify 'Body' is in url")
def verify_body_in_url(context):
    context.app.header.verify_body_in_url()