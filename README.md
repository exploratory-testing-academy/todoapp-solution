# To Do App -solution

To Do App is a popular application spec used to create frontend framework technology demos. In some ways, when developers show off tech to other developers and the project comes populated with a browser test suite of its own to run, you would think they work pretty well. This repo starts with the premise of testing that assumption, but testing some of the to do app versions. 

The style of testing this repository showcases is *contemporary exploratory testing*. This means it aims at showing both the results, the reporting and the automation to leave behind as a result of having tested the application. The examples here are created through using the to do application versions for interviewing for tester positions and teaching testers. For interviewing purposes, it would be great if people knew to look for a reference but so far that has not been the case. 

The implementations of To Do App are available with https://todomvc.com and a version with intentionally added bugs is available with https://todolist.james.am/

This solution document is made available with Creative Commons Attribution Non-Commercial Sharealike 
https://creativecommons.org/licenses/by-nc-sa/4.0/ and for more permissive licenses, contact CGI Suomi Oy / Maaret Pyhäjärvi. 

## The Assignment for the Exercise

For newbies, I use a target for testing as a take at home assignment, asking to use less than two hours to showcase their work. 
For seasoned, I use a target for testing as an in-interview exercise, limited in time, to showcase how they would approach work. 

Developer community uses To Do App to showcase different technical framework implementations. Here's two different implementations of the To Do App for you to test and showcase your testing work. 

* Elm: https://todomvc.com/examples/elm/
* Angular: https://todolist.james.am/#/

As a result of your testing, please provide: 

* A clearly catalogued listing of identified issues you’d like to give as feedback to whoever authored the version
* Listing of features you recognize while you test
* Description of how you ended up doing the assignment
* (optional) example of test automation in language and framework of your choice

## Principles for assessment

There are multiple routes to the same destination. You are assessing structuring of routes as much as getting to the destination. The candidate can do well by starting without automation as much as with automation, or research of the application, if they *explain their choice* and the choices are actively made. 

When observing testing, there is always a time-box you end up investing. You are expected to do your best work within the time you are given.

There should be an idea of coverage - types of things you do, types of bugs you look for, listing of features and data. When testing, you can decide to stop when your idea of coverage is complete, and miss bugs. The exercise searches for your model of stopping criteria. 

## Assignment Assessment Grid

Score a point againts each criteria. Expect a candidates claiming extensive exploratory testing experience to score higher. All items are teachable, so for a seasoned candidate missing a criteria, introduce the criteria and assess if they learn as they test. 

### ESSENTIAL INSIGHTS

* Architecture: frontend only
* Same spec for both implementations
* Material online to reuse
* Reading the room, clarifying assumptions
* Optional is chance to show more
* Presenting your work is not just description of doing

### ESSENTIAL ACTIONS

* Research: find the spec as it is online
* Research: ask questions
* Meta: explain what and why you do
* Learning: showing something changed in knowledge while testing
* Bias to action: balance explaining and results
* Modeling function, data, environments
* Recognizing tools of environment
* Choosing a constraint to control perspective
* Stopping criteria: time or coverage
* Classifying and prioritizing
* Clarity of reporting issues
* Reporting per implementation and common for both
* TL;DR - expect lazy readers
* Using and explaining a heuristic
* Awareness of classes of data (e.g. naughty strings)
* Surprise me (e.g. screenshot to genAI)

### RESULTS
* Functional problems (e.g. off by one count, select all, tooltip)
* Functional problem, browser dimension (e.g persistence, icon corruption, consecutive add)
* Usability problems (e.g. light colors, lack of instructions)
* Implementation problems (on console) e.g. messages in code and errors in console
* Data-related problems: creating empty items / items with whitespace
* Data-related problems: special characters
* Missing features (e.g. order items)
* Typos
* In-app consistency (e.g. always visible functionality that does not always work)

### AUTOMATION

* Working with selectors
* Reading error messages
* Scenario selection
* Locators
* Structure and naming
* Describing choices
* Readme for getting tests to run
* Choices of clean browser between tests
* Assert for correctness

### MISTAKES THAT NEED EXPLAINING

* Overfocus on locators while application is unknown and automation is not in play
* Wanting to input SQL injection string
* Considering right functionality a bug
* Inability to recognize a broken function comparing the two different implementations

## Listing of features

40 claims collected to 10 features. Any other way of separating features and claims is as good as this. Listing is a combination of what the To Do App -project lists as developer intent through their tests, what they list as their specs in their documentation and exploring and naming features and claims observed that need testing. 

No Todos

    ✓✓ should hide #main and #footer

New Todo

    ✓✓ should autofocus to enter todo items on page load

    ✓✓ should allow to add todo items

    ✓✓ should clear text input field when an item is added 

    ✓✓ should trim text input

    ✓✓ should show #main and #footer when items added 

    ✓✓ should show placeholder text

    ✓✓ should allow adding todo items of varying length and content

    ✓✓ should not allow creating empty todo items

Mark all as completed

    ✓ should allow to mark all items as completed

    ✓ should default to marking completed if any items are incomplete

    ✓ should allow to clear the completion state of all items

    ✓ complete all checkbox should update state when items are completed 

Item

    ✓ should allow to mark items as complete 

    ✓ should allow to un-mark items as complete 

    ✓ should allow to edit an item 

    ✓ should show the remove button on hover

Editing

    ✓ should hide other controls when editing 

    ✓ should save edits on enter 

    ✓ should save edits on blur 

    ✓✓ should trim entered text 

    ✓ should remove the item if an empty text string was entered 

    ✓ should cancel edits on escape 

Delete

    ✓✓ should show delete on hover over

    ✓✓ should delete selected line

Counter

    ✓ should display the current number of todo items

    ✓ should have singular (one) and plural (zero, many) forms of item(s) without exclamation mark

    ✓ should have number of items wrapped in strong-tag

Clear completed

    ✓ should display the number of completed items

    ✓ should remove completed items when clicked

    ✓ should be hidden when there are no items that are completed

Persistence

    ✓✓ should persist its data in local storage

Filter / Routing

    ✓ should allow to display active items

    ✓ should allow to display completed items

    ✓ should allow to display all items 

    ✓ should highlight the currently applied filter

    ✓ should be visible in URL

    ✓ should allow for route #!/

    ✓ should be applied on item state changes without refresh

    ✓ should be persisted on reload

## Listing of issues

### For Elm: https://todomvc.com/examples/elm/

* [ CORRECTNESS OF FUNCTION ] Select all does not work. Clicking on the icon does nothing. 
* [ CORRECTNESS OF FUNCTION ] Edit mode cannot be escaped with esc
* [ CORRECTNESS OF FUNCTION ] Unsaved new item not removed on refresh
* [ CORRECTNESS OF FUNCTION ] Adding space adds empty item
* [ CORRECTNESS OF FUNCTION ] Edit to empty leaves the item while it should be removed
* [ LAYOUT ] Edit to empty messes the layout and I should not see it since empty should not be added
* [ IMPLEMENTATION ] Warning about compiled in DEV mode
* [ CORRECTNESS OF FUNCTION ] Browser back / forward with routes/filters does not update the contents of the page

FAILING CLAIMS

✓ New todo should not allow creating empty todo items

✓ Mark all as completed should allow to mark all items as completed

✓ Mark all as completed should default to marking completed if any items are incomplete

✓ Mark all as completed should allow to clear the completion state of all items

✓ Mark all as completed complete all checkbox should update state when items are completed 

✓ Editing should remove the item if an empty text string was entered 

✓ Editing should cancel edits on escape 

✓ Filter / Routing should allow for route #!/

### Angular: https://todolist.james.am/#/

* [ TYPO ] Incorrectly written word in placeholder text: "need's" => "needs"
* [ TYPO ] Incorrectly capitalized word in filters text: "active" => "Active" to be consistent with others
* [ TYPO ] Incorrectly written word in instructions: "toodo" => "todo"
* [ CORRECTNESS OF FUNCTION ] Counter for items miscalculates to one item less than available on the list
* [ CORRECTNESS OF FUNCTION ] Select all does not unselect all on 2nd click, only on third click
* [ CORRECTNESS OF FUNCTION ] Clear does not clear items, it clears only completed items
* [ CORRECTNESS OF FUNCTION ] Clear completed / Clear -button should only be visible / active when it can be used.  
* [ CORRECTNESS OF FUNCTION ] Placeholder text vanishes after inserting an item and it should always be visible when items can be added; returns on refresh.
* [ CORRECTNESS OF FUNCTION ] Select all and delete buttons get corrupted given enough time on application and using refresh; ~ for delete, sideways Å for delete.
* [ CONSISTENCY ] Adding multiple items on list adds spaces in the item entry 
* [ TERMINOLOGY ] Since "Clear" only clears completed items, it should be called "Clear completed"
* [ DATA ] Adding whitespace while editing does not trim the whitespace but trims on displaying the text on UI. 
* [ IMPLEMENTATION ]`<!-- STUPID APP -->` in comments is probably intentionally added for fun
* [ IMPLEMENTATION ] "ToDo: Remove this eventually" tooltip is probably added for fun as well
* [ IMPLEMENTATION ] Errors on missing resources on console are probably added for fun too
* [ UNIMPLEMENTED ] "Clear" is missing the counter after it the spec asks for
* [ UNIMPLEMENTED ] No route #!/, a technology-specific routing to main page without reload 
* [ NOTE ] URL does not follow the technology pattern you would expect for the demo app of angular.


FAILING CLAIMS

✓ New Todo should show placeholder text

✓ Mark all as completed should allow to clear the completion state of all items

✓ Counter should display the current number of todo items

✓ Clear completed should display the number of completed items

✓ Clear completed should be hidden when there are no items that are completed

✓ Filter / Routing should allow for route #!/

### For Both Elm: https://todomvc.com/examples/elm/ and Angular: https://todolist.james.am/#/

* [ ACCESSIBILITY ] Light color scheme hard to read as contrast to background is low
* [ NEW FEATURE REQUEST ] Reordering items to show prioritization of to do does not exist
* [ NEW FEATURE REQUEST ] Word wrapping is not supported, words are cut in middle of the space allocated into two lines
* [ NEW FEATURE REQUEST ] Limiting visible length of a todo item
* [ NEW FEATURE REQUEST ] Duplicate detection
* [ NEW FEATURE REQUEST ] Application does not scale nicely to smaller screen size, make it responsive
* [ NEW FEATURE REQUEST ] No undo
* [ NEW FEATURE REQUEST ] No confirm on clear and delete
* [ NEW FEATURE REQUEST ] Long text edit popup that shows whole text
* [ NEW FEATURE REQUEST ] Pagination
* [ USABILITY ] Items are added at end of list not top of the list, and latest additions could be on top
* [ USABILITY ] Concepts of "active" and "completed" may not be common terms and better term options could be investigated
* [ USABILITY ] Application does not allow adding a to do item with a mouse. The text needs to be written on keyboard anyway, but a user may be used to expecting a button. 
* [ USABILITY ] Filters / router functionality can be confusing, as the user does not clearly understand the three filters on bottom. User may have a filter of completed on when adding a new one, and the item vanishing can be confusing.
* [ USABILITY ] Stacked shadow effect in the bottom makes it seem like there are multiple layers. That does not connect well with the filters / routing functionality.
* [ USABILITY ] Delete, edit and select all options take some discovering. 
* [ USABILITY ] Deletion is only available on select and hover, and deleting multiple items at a time is not possible
* [ ACCESSIBILITY ] Delete unavailable with keyboard only, keyboard use not supported
* [ DATA ] `ด้้้้้็็็็็้้้้้็็็็็้้้้้้้้็็็็็้้้้้็็็็็้้้้้้้้็็็็็้้้้้็็็็็้้้้้้้้็็็็็้้้้้็็็็` does not copy a single character but an encoded mess
* [ LAYOUT ] Long text and delete button would look better if they were separated into own columns
* [ DATA ] Some text selection get delete icon on top of text
* [ CONSISTENCY ] Click icon for items that can be selected is hand on bottom, regular on other selections

### For React https://todomvc.com/examples/react/dist/

(not tested consistently)

* [ DATA ] Special characters ', #, & get encoded to the app UI as `&#x27;&quot;&amp;`

## Test automation

Instructions from a mac: 

Start with virtual environment
`python3 -m venv .venv`
`source .venv/bin/activate`

Install dependencies
`pip install -r requirements.txt`
`playwright install`

Configure pytest as runner locally to run from tests add on or command line
`pytest`

Scope: 

* Single test for adding to do item, parametrized
* Single test with add and delete, parametrized to two