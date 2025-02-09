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


"""
✓ New Todo should show #main and #footer when items added 
"""

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


"""
✓ New Todo should clear text input field when an item is added 
"""

def test_new_todo_should_clear_text_input_field(br_page: Page):
    br_page.click('.new-todo')
    br_page.fill('.new-todo', 'item')
    br_page.locator('.new-todo').press('Enter')
    expect(br_page.locator('.new-todo')).to_be_empty()


"""
✓ New todo should show placeholder text
"""

def test_new_todo_should_show_placeholder_text(br_page: Page):
    expect(br_page.locator('.new-todo')).to_have_attribute('placeholder', 'What needs to be done?')


def test_new_todo_should_show_placeholder_text_after_adding_items(br_page: Page):
    br_page.fill('.new-todo', 'something to the list')
    br_page.locator('.new-todo').press('Enter')
    expect(br_page.locator('.new-todo')).to_have_attribute('placeholder', 'What needs to be done?')


"""
✓ New todo should trim text input
"""

def test_new_todo_should_trim_text_input(br_page: Page):
    br_page.fill('.new-todo', '  item  with    spaces')
    br_page.locator('.new-todo').press('Enter')
    expect(br_page.locator('ul.todo-list')).to_have_text('item with spaces')


"""
✓ Editing should trim entered text 
"""

def test_editing_todo_should_trim_text_input(br_page: Page):
    br_page.fill('.new-todo', 'item')
    br_page.locator('.new-todo').press('Enter')
    br_page.locator('ul.todo-list').dblclick()
    br_page.fill('.edit', '  item  with    spaces')
    br_page.locator('.edit').press('Enter')
    expect(br_page.locator('ul.todo-list')).to_have_text('item with spaces')
    br_page.locator('ul.todo-list').dblclick()
    expect(br_page.locator('.edit')).to_have_value('  item  with    spaces')


"""
✓ New todo should allow adding todo items of varying length and content
"""

def test_new_todo_long_text(br_page: Page):
    br_page.fill('.new-todo', 'item ' * 100)
    br_page.locator('.new-todo').press('Enter')
    expect(br_page.locator('ul.todo-list')).to_have_text('a' * 100)

def test_new_todo_long_text(br_page: Page):
    br_page.fill('.new-todo', 'hi you four times caster chanter disaster hopskotch teddybears fluctuation aboriginally contradictory electronically')
    br_page.locator('.new-todo').press('Enter')
    expect(br_page.locator('ul.todo-list')).to_have_text('hi you four times caster chanter disaster hopskotch teddybears fluctuation aboriginally contradictory electronically')

def test_new_todo_with_scandinavian_chars(br_page: Page):
    br_page.fill('.new-todo', 'Pyhäjärvi å')
    br_page.locator('.new-todo').press('Enter')
    expect(br_page.locator('ul.todo-list')).to_have_text('Pyhäjärvi å')

def test_new_todo_special_chars(br_page: Page):
    br_page.fill('.new-todo', '!@#$%^&*()_+')
    br_page.locator('.new-todo').press('Enter')
    expect(br_page.locator('ul.todo-list')).to_have_text('!@#$%^&*()_+')

def test_new_todo_with_emojis(br_page: Page):
    br_page.fill('.new-todo', '👍👍👍👍👍')
    br_page.locator('.new-todo').press('Enter')
    expect(br_page.locator('ul.todo-list')).to_have_text('👍👍👍👍👍')


"""
✓ New todo should not allow creating empty todo items
"""

def test_new_todo_empty_text(br_page: Page):
    br_page.fill('.new-todo', ' ')
    br_page.locator('.new-todo').press('Enter')
    expect(br_page.locator('ul.todo-list')).not_to_be_visible()
    expect(br_page.locator(".main")).not_to_be_visible()
    expect(br_page.locator(".footer")).not_to_be_visible()
