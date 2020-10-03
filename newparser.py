from selenium import webdriver

# выводит текст объявлений с первой страницы запроса
class ProgParser(object):

    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        self.go_to_page()

    def go_to_page(self):
        self.driver.get('https://www.avito.ru/moskva_i_mo/velosipedy?q=%D0%BA%D0%B0%D0%BC%D0%B5%D1%80%D0%B0+27')
        slide_elems = self.driver.find_elements_by_class_name("snippet-link-name")

        for elem in slide_elems:
            print(elem.text)


def main():
    path_to_driver = 'chromedriver.exe'
    driver = webdriver.Chrome(path_to_driver)
    parser = ProgParser(driver)
    parser.parse()


if __name__ == '__main__':
    main()