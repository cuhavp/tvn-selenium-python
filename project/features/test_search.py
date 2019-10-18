from project.pages.search import GoogleSearchPage


def test_google_search(browser):
    search_page = GoogleSearchPage(browser)
    on(GoogleSearchPage(browser)).search_box_txt_element.send_keys("panda\n")
    search_page.open('')
    search_page.search("panda\n")
