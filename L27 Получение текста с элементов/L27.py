from playwright.sync_api import sync_playwright, Page, expect

URL_BTN = 'https://demoqa.com/buttons'
URL_TEXT_BOX = 'https://demoqa.com/text-box'
Btn_Double_Click_Me = 'Double Click Me'
text_click_me = 'You have done a dynamic click'
URL_Select_Menu = 'https://demoqa.com/select-menu'
# 27x01: «Текст кнопки» (Buttons)
URL_text_box = 'https://demoqa.com/text-box'
URL_the_int_hero = 'https://the-internet.herokuapp.com/'
URL_THE_INT_LOGIN = 'https://the-internet.herokuapp.com/login'
URL_THE_INT_CHECKBOX = 'https://the-internet.herokuapp.com/checkboxes'

URL_DYNAMIC_LOADING_2 = 'https://the-internet.herokuapp.com/dynamic_loading/2'
URL_IFRAME = 'https://the-internet.herokuapp.com/iframe'
# def base_page():
#     with sync_playwright() as drv:
#         browser = drv.chromium.launch(headless=False, slow_mo=1000)
#         page = browser.new_page()
#         page.goto(URL_BTN)


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
        assert "Optimus Prime" in value_dropdown

        print(f'{value_dropdown}')

# Страница: https://demoqa.com/text-box
# Задача:
# 1. Откройте страницу.
# 2. Найдите лейбл «Current Address».
# 3. Получите его текст через .inner_text() и .text_content().
# 4. Сравните результаты (выведите через repr()).
# 5. Объясните, есть ли разница (должны быть одинаковы для видимого текста).
# Что тренируем:
# Разницу между .inner_text() и .text_content()
#
# Отладку через repr()


def test_task_05():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_text_box, wait_until="domcontentloaded")
        a1 = page.get_by_placeholder("Current Address").inner_text()
        a2 = page.get_by_placeholder("Current Address").text_content()
        print(repr(a1))
        print(repr(a2))


# Страница: https://the-internet.herokuapp.com/
# Задача:
# 1. Откройте главную страницу.
# 2. Получите заголовок <h3> через .inner_text().
# 3. Проверьте, что заголовок содержит "Available Examples".
# 4. Используйте expect().to_contain_text().
# Что тренируем:
# Базовое получение текста
#
# Частичное совпадение через to_contain_text()
def test_task_06():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_the_int_hero)
        loc_h3 = page.locator("h2")
        text_h3 = loc_h3.inner_text()
        # expect(page.get_by_role("heading", name="Available Examples")).\to_be_visible
        expect(loc_h3).to_contain_text('Available Examples')
        # assert 'Available Examples' in text_h3
        print(text_h3)


def test_task_07():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_THE_INT_LOGIN)
        user_name = page.locator('#username')
        user_name.fill('tomsmith')
        user_password = page.locator('#password')
        user_password.fill('SuperSecretPassword')
        btn_login = page.locator('[type="submit"]')
        btn_login.click()
        error = page.locator('#flash')
        assert 'Your password is invalid!' in error.inner_text()


def test_task_08():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_THE_INT_LOGIN)
        user_name = page.locator('#username')
        user_name.fill('tomsmith')
        user_password = page.locator('#password')
        user_password.fill('SuperSecretPassword!')
        btn_login = page.locator('[type="submit"]')
        btn_login.click()
        success = page.locator('[class="subheader"]')
        success.inner_text()
        assert 'Welcome to the Secure Area' in success.inner_text()
        success.input_value()
        print(success.input_value())


def test_task_09():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_THE_INT_CHECKBOX)
        checkbox = page.locator('input [type= "checkbox"]')
        count = checkbox.count()
        print(f"Количество чекбоксов: {count}")
        # for i in range(count):
        #     cb = checkbox.nth(i)
        #
        #     state = "checked ✅" if cb.is_checked() else "unchecked ❌"
        #     print(f"Checkbox {i + 1}: {state}")
        #
        #     # текст страницы (подписей тут почти нет, но можно взять весь текст)
        # text = page.locator("#checkboxes").inner_text()
        # print("\nТекст блока:")
        # print(text)


def test_task_10():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_DYNAMIC_LOADING_2)
        page.locator('#start button').click()
        expect(page.locator('#finish')).to_have_text('Hello World!')
        text = page.locator('#finish').inner_text()
        print(text)


def test_task_11():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL_IFRAME)
        page.frame_locator('#iframe').locator('body[data-id="mce_0"]')
        text = page.frame_locator('#iframe').locator('body[data-id="mce_0"]')\
            .inner_text()
        print(text)


if __name__ == "__main__":
    test_task_11()

