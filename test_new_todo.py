from playwright.sync_api import expect
from playwright.sync_api import Page
import pytest

@pytest.mark.parametrize("input_text", ["milk"], ids=["one"])
def test_new_todo(br_page: Page, input_text):
    br_page.fill("input.new-todo", input_text)
    br_page.press("input.new-todo", "Enter")
    expect(br_page.locator("ul.todo-list")).to_have_text(input_text)