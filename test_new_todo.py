from playwright.sync_api import expect
from playwright.sync_api import Page
import pytest

"""
✓ New todo should allow to add todo items
✓ Delete should show delete on hover over
✓ Delete should delete selected line
"""

@pytest.mark.parametrize("input_text", ["milk", "milkshake"], ids=["one", "two"])
def test_add_and_remove_todo(br_page: Page, input_text):
    br_page.fill("input.new-todo", input_text)
    br_page.press("input.new-todo", "Enter")
    expect(br_page.locator("ul.todo-list")).to_have_text(input_text)
    br_page.locator("ul.todo-list").hover()
    br_page.locator(".destroy").click()
    expect(br_page.locator("ul.todo-list")).not_to_have_text(input_text)
    

"""
✓ Counter should display the current number of todo items
"""

def test_add_five_todos_and_verify_count(br_page: Page):
    for i in range(5):
        br_page.fill("input.new-todo", f"todo {i+1}")
        br_page.press("input.new-todo", "Enter")
    expect(br_page.locator('.todo-count')).to_contain_text('5')


"""
✓  No Todos should hide #main and #footer
"""

def test_no_todos_should_hide_main_and_footer(br_page: Page):
    expect(br_page.locator(".main")).not_to_be_visible()
    expect(br_page.locator(".footer")).not_to_be_visible()


def test_one_todo_brings_main_and_footer(br_page: Page):
    br_page.fill("input.new-todo", "todo 1")
    br_page.press("input.new-todo", "Enter")
    expect(br_page.locator(".main")).to_be_visible()
    expect(br_page.locator(".footer")).to_be_visible()
    br_page.locator("ul.todo-list").hover()
    br_page.locator(".destroy").click()
    expect(br_page.locator(".main")).not_to_be_visible()
    expect(br_page.locator(".footer")).not_to_be_visible()


"""
✓  New Todo should autofocus to enter todo items on page load
"""
def test_new_todo_should_autofocus(br_page: Page):
    expect(br_page.locator(".new-todo")).to_be_focused()


"""
✓ Delete should show delete on hover over
✓ Delete should delete selected line
"""
def test_delete_should_show_delete_on_hover_over(br_page: Page):
    br_page.fill("input.new-todo", "todo 1")
    br_page.press("input.new-todo", "Enter")
    expect(br_page.locator(".destroy")).not_to_be_visible()
    br_page.locator("ul.todo-list").hover()
    expect(br_page.locator(".destroy")).to_be_visible()
    br_page.locator(".destroy").click()
    expect(br_page.locator("ul.todo-list")).not_to_have_text("todo 1")

"""
✓ Persistence should persist its data in local storage
"""

def test_persistence_should_persist_data_in_local_storage(br_page: Page):
    br_page.fill("input.new-todo", "todo 1")
    br_page.press("input.new-todo", "Enter")
    br_page.reload()
    expect(br_page.locator("ul.todo-list")).to_have_text("todo 1")


#pytest skip
@pytest.mark.skip(reason="Exploring to reveal long fuse bug, not worth leaving behind in CI")
def test_repeated_refreshes_corrupt_selectall_delete_buttons(br_page: Page):
    br_page.fill("input.new-todo", f"todo 1")
    br_page.press("input.new-todo", "Enter")
    for i in range(10):
        br_page.reload()
    expect(br_page.locator("ul.todo-list")).to_have_text("todo 1")
    #verify icon styles for delete and select all
    expect(br_page.locator(".destroy")).to_have_style("display", "none")
    expect(br_page.locator(".toggle-all")).to_have_style("display", "none")
