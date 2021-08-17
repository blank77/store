import time
class Method:
    def __init__(self,driver):
        self.driver = driver

    def register(self):
        time.sleep(12)
        self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click()
        time.sleep(2)
        for i in range(4):
            self.driver.swipe(500, 1200, 500, 300)
            time.sleep(10)
