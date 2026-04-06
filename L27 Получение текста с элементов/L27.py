from playwright.sync_api import sync_playwright, Page, expect

URL_BTN = 'https://demoqa.com/buttons'
URL_TEXT_BOX = 'https://demoqa.com/text-box'
Btn_Double_Click_Me = 'Double Click Me'
text_click_me = 'You have done a dynamic click'
URL_Select_Menu = 'https://demoqa.com/select-menu'
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


# Страница:https://demoqa.com/text-box
# Задача:
# 1. Откройте форму «Text Box».
# 2. Введите ваше имя в поле «Full Name» (через .fill()).
# 3. Введите email в поле «Email».
# 4. Прочитайте значения обоих полей через .input_value().
# 5. Выведите их в консоль в формате: "Имя: ..., Email: ..."
# Что тренируем:
# Использование .input_value() для полей ввода
#
# Чтение данных из формы

def test_task_03():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_TEXT_BOX)
        page.get_by_placeholder("Full Name").fill("Orom")
        page.get_by_placeholder("name@example.com").fill("orom@gmail.com")
        print("поля заполнили")
        value1 = page.locator("#userName").input_value()
        value2 = page.locator("#userEmail").input_value()
        print(f"Имя:{value1}, Email:{value2}")


# Страница:https://demoqa.com/select-menu
# Задача:
# 1. Откройте страницу «Select Menu».
# 2. Найдите все опции в стандартном выпадающем списке.
# 3. Получите тексты всех опций через .all_inner_texts().
# 4. Выведите список в консоль.
# 5. Проверьте, что в списке есть опция "Optimus Prime".
# Что тренируем:
# Метод .all_inner_texts() для списков
#
# Проверку наличия элемента в списке
def test_task_04():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_Select_Menu)
        selected1 = page.locator("#withOptGroup")
        selected1.click()
        value_dropdown = selected1.all_inner_texts()
        selected2 = page.locator("#selectOne")
        selected2.click()
        value2_dropdown = selected2.all_inner_texts()
        # assert 'Optimus Prime' in value_dropdown and value2_dropdown
        print(f'{value_dropdown}, {value2_dropdown}')

        # page.get_by_placeholder("Full Name").fill("Orom")
        # page.get_by_placeholder("name@example.com").fill("orom@gmail.com")
        # print("поля заполнили")
        # value1 = page.locator("#userName").input_value()
        # value2 = page.locator("#userEmail").input_value()
        # print(f"Имя:{value1}, Email:{value2}")


if __name__ == "__main__":
    test_task_04()

