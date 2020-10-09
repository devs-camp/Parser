import commonlib
from settings import *
import urllib.request
from selenium import webdriver
import os
from time import sleep

class VkGrabber:
    def __init__(self,id, scrollTimes, saveFolder):
        self.__initChrome()
        self.__openPage(id)
        self.__scroll(scrollTimes)
        self.saveFolder = saveFolder

    def grabPosts(self):
        self.__grabPosts_internal(self.saveFolder)

    def __initChrome(self):
        self.driver = webdriver.Chrome(DRIVER)

    def __openPage(self, id):
        self.driver.get(id)
        commonlib.printProgress(2)

    def __scroll(self, times):
        for i in range(times):
            height = self.driver.execute_script("return document.body.scrollHeight;")
            self.driver.execute_script(f"window.scrollTo(0, {height});")
            sleep(1)
            commonlib.printProgress(2)

    def __grabPosts_internal(self, saveFolder):
        try:
            postNodes = self.driver.find_elements_by_class_name("post")
            for postnum, post in enumerate(postNodes):
                postnum = "post" + str(postnum)
                folderForPost = os.path.join(saveFolder, postnum)
                commonlib.createFolder(folderForPost)
                #получить тест из поста
                try:
                    commonlib.printProgress(1)
                    text = post.find_element_by_class_name("wall_post_text").text
                    commonlib.saveFile(commonlib.subfile(folderForPost,"text.txt"), text)
                except Exception as e:
                    commonlib.saveFile(commonlib.subfile(folderForPost,"text_grab_error.txt"), str(e))

                #получить все изображения
                try:
                    imagesParent = post.find_element_by_class_name("page_post_sized_thumbs")
                    picsA = imagesParent.find_elements_by_tag_name("a")
                    for index, picNode in enumerate(picsA):
                        commonlib.printProgress(1)
                        # получить ссылку на pic
                        link = self.__parsePicText(picNode)
                        # download the image
                        urllib.request.urlretrieve(link, commonlib.subfile(folderForPost,f"{postnum}_image{index}.jpg"))
                except Exception as e:
                    commonlib.saveFile(commonlib.subfile(folderForPost, "no_image.txt"), str(e))
        finally:
            self.driver.close()

    def __parsePicText(self, picNode):
        onclick = picNode.get_attribute("onclick")
        linkStrIndex = onclick.find('{"temp":{"x":"') + 14
        linkStrIndexEnd = onclick.find('",', linkStrIndex)
        return onclick[linkStrIndex:linkStrIndexEnd].replace("\\", "")