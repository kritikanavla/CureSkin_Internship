
from behave import given, when, then


@when("Search for the footer links under Our Policy list")
def search_footer_links(context):
    context.app.footer.search_footer_links()
@then("Click and verify it navigates to correct pages")
def click_on_links_verify_page(context):
    context.app.footer.click_on_links_verify_page()
