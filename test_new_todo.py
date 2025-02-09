from playwright.sync_api import expect
from playwright.sync_api import Page
import pytest

@pytest.mark.parametrize("input_text", ["milk", "milkshake"], ids=["one", "two"])
def test_add_and_remove_todo(br_page: Page, input_text):
    br_page.fill("input.new-todo", input_text)
    br_page.press("input.new-todo", "Enter")
    expect(br_page.locator("ul.todo-list")).to_have_text(input_text)
    br_page.locator("ul.todo-list").hover()
    br_page.locator(".destroy").click()
    expect(br_page.locator("ul.todo-list")).not_to_have_text(input_text)