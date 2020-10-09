from settings import *
from vkGrabber import VkGrabber
import commonlib

page = "https://vk.com/id1"
vkGrabber = VkGrabber(page, 1, commonlib.subdir(ROOT_DIR, "posts"))
vkGrabber.grabPosts()

print("done")