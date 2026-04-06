from playwright.sync_api import sync_playwright, Page, expect

URL_BTN = 'https://demoqa.com/buttons'
Btn_Double_Click_Me = 'Double Click Me'
text_click_me = 'You have done a dynamic click'
# 27x01: «Текст кнопки» (Buttons)


def test_task_01():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_BTN)
        # expect(page.locator("div")).to_have_text("Hello World")
        text = page.locator("text=Double Click Me").inner_text()
        print(text)

        assert text in Btn_Double_Click_Me


# #Страница:https://demoqa.com/buttons
# Задача:
# 1. Кликните по кнопке «Click Me» один раз.
# 2. Дождитесь появления сообщения под кнопкой (используйте expect().to_have_text()).
# 3. Получите текст сообщения через .inner_text().
# 4. Проверьте, что текст содержит "You have done a right click" (или другое, в зависимости от кнопки).
# Что тренируем:
# Ожидание появления текста через expect()
#
# Чтение динамического контента

def test_task_02():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_BTN)
        page.get_by_text("Click Me", exact=True).click()
        print("кнопкпу нажали")
        expect(page.locator("#dynamicClickMessage")).\
            to_have_text(text_click_me)
        print("текст совппапдает")





        # button = page.locator("text=Click Me")
        # # text = button.inner_text()
        # print(f"{button} найден")
        # button.click()
         # assert_text_in_btn(page.url, Btn_Double_Click_Me)
    #     loc_h1 = page.locator("h1.heading")
    #     text_h1 = loc_h1.text_content()
    #     assert TEXT_TO_FIND in text_h1, \
    #     f"Не тот заголовок!\n" \
    #     f"Ожидание: '{TEXT_TO_FIND}' в заголовке\n" \
    #     f"Актуальный текст заголовка: '{text_h1}'"
    # print(f"T1: ✅ Сайт доступен. Заголовок: '{text_h1}'")


if __name__ == "__main__":
    test_task_02()

