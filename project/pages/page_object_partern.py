import re
import time
import warnings
import inspect
from selenium.common.exceptions import NoSuchElementException


class PageObjectPattern(object):
    driver = None

    def __init__(self, *args, **kwargs):
        elements = [{var: value} for var, value in self.__class__.__dict__.items() if isinstance(value, tuple)]
        for element in elements:
            for name, locator in element.items():
                self.set_func(name, locator)

    def __getattr__(self, method_name):
        if method_name.endswith('_element') or method_name.endswith('_elements'):
            callable_method_name = "self.%s" % re.sub("_element.*", "", method_name)
            if callable(eval(callable_method_name)):
                func = eval(callable_method_name)
                return func()
        elif method_name.startswith('found'):
            callable_method_name = "self.%s" % re.sub("found_", "", method_name)
            if callable(eval(callable_method_name)):
                func = eval(callable_method_name)
                locator = inspect.getclosurevars(func).nonlocals['locator']
                return lambda: self.have_element_displayed(locator[0], locator[1])
        elif method_name.startswith('locate_element'):
            callable_method_name = "self.%s" % re.sub("locate_element_", "", method_name)
            if callable(eval(callable_method_name)):
                return eval(callable_method_name)
        else:
            raise AttributeError(method_name)

    def set_func(self, method_name, locator):
        driver = self.driver

        def locate_and_cache_element():
            if method_name.endswith('s') or '_list' in method_name:
                elements = self.locate_element(driver, locator[0], locator[1], multiple=True)
                setattr(self, 'cached_%s' % method_name, elements)
                return elements
            else:
                element = self.locate_element(driver, locator[0], locator[1])
                setattr(self, 'cached_%s' % method_name, element)
                return element
        locate_and_cache_element.__name__ = method_name
        setattr(self, method_name, locate_and_cache_element)

    def retry_locate_async_element(self, element, unexpected_text='None'):
        retry = 0
        while element.text == unexpected_text and retry < 5:
            retry += 1
            time.sleep(1)
            self.wait_for_ajax_completed()
        if retry > 1:
            warnings.warn('The element %s has been retried locating %s times' % (element, retry))
        return element

    @staticmethod
    def locate_element(driver, by, locator, multiple=False):
        end_time = time.time() + 3
        while True:
            try:
                if multiple:
                    return driver.find_elements(by, locator)
                else:
                    return driver.find_element(by, locator)
            except Exception as ex:
                message = "An exception of type {0} occurred. Arguments:\n{1!r}".format(type(ex).__name__, ex.args)
            time.sleep(0.3)
            if time.time() > end_time:
                break
        raise NoSuchElementException(message)