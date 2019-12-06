from idlelib import browser

def radioClick(self):
    # _val = self.elementClick(self._radio_id, locatorType="id")
    _val = browser.find_elements_by_xpath("//input[@type='radio'] ")
    print(_val)