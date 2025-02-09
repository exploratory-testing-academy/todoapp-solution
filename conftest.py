import pytest
from playwright.sync_api import Browser, Page, BrowserContext
import os
from slugify import slugify


@pytest.fixture(scope="session", autouse=True)
def url(pytestconfig):
    url = None
    if url is None:
        url = pytestconfig.getoption("base_url")
    yield url


@pytest.fixture(scope="function")
def br(browser: Browser, my_context_arguments, pytestconfig, request: pytest.FixtureRequest) -> BrowserContext:
    new_context = browser.new_context(**my_context_arguments)
    new_context.tracing.start(snapshots=True, screenshots=True)
    yield new_context
    new_context.tracing.stop(path=_build_result_folder(pytestconfig, request, "trace.zip"))
    new_context.close()


@pytest.fixture(scope="function")
def br_page(br, url) -> Page:
    new_page = br.new_page()
    new_page.goto(url)
    yield new_page


@pytest.fixture(scope="session")
def my_context_arguments(url):
    context_args = {
        "base_url": url,
        "locale": "fi-FI",
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
        "java_script_enabled": True,
    }
    return context_args

def _build_result_folder(pytestconfig, request: pytest.FixtureRequest, folder_or_file_name: str) -> str:
    return os.path.join(pytestconfig.getoption("--output"), slugify(request.node.name), folder_or_file_name)