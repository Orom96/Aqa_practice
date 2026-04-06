from playwright.sync_api import sync_playwright, Page

URL_BTN = 'https://demoqa.com/buttons'
Btn_Double_Click_Me = 'Double Click Me'
# 27x01: «Текст кнопки» (Buttons)


def test_task_01(page: Page):
    page.goto(URL_BTN)
    text = page.locator("text=Double Click Me").inner_text()
    #     assert_text_in_url(page.url, Btn_Double_Click_Me)
    #     loc_h1 = page.locator("h1.heading")
    #     text_h1 = loc_h1.text_content()
    #     assert TEXT_TO_FIND in text_h1, \
    #     f"Не тот заголовок!\n" \
    #     f"Ожидание: '{TEXT_TO_FIND}' в заголовке\n" \
    #     f"Актуальный текст заголовка: '{text_h1}'"
    # print(f"T1: ✅ Сайт доступен. Заголовок: '{text_h1}'")


# if __name__ == "__main__":
#     test_task_01()

