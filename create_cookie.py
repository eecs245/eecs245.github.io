from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://leccap.engin.umich.edu/leccap/site/0t929w2oc176a98jk69")
    input("Finish UMich login in the browser, then press Enter here...")
    context.storage_state(path=".leccap_storage_state.json")
    browser.close()
print("Saved .leccap_storage_state.json")