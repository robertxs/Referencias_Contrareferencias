# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Selenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_selenium(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("//a[@id='registrarse']/b").click()
        driver.find_element_by_id("id_first_name").click()
        driver.find_element_by_id("id_first_name").clear()
        time.sleep(1)
        driver.find_element_by_id("id_first_name").send_keys("Luis")
        driver.find_element_by_id("id_last_name").click()
        driver.find_element_by_id("id_last_name").clear()
        time.sleep(1)
        driver.find_element_by_id("id_last_name").send_keys("Gomez")
        driver.find_element_by_id("id_email").click()
        driver.find_element_by_id("id_email").clear()
        time.sleep(1)
        driver.find_element_by_id("id_email").send_keys("luis@gmail.com")
        driver.find_element_by_id("id_rol").click()
        driver.find_element_by_xpath("//option[@value='admin']").click()
        driver.find_element_by_id("id_ci").click()
        driver.find_element_by_id("id_ci").clear()
        time.sleep(1)
        driver.find_element_by_id("id_ci").send_keys("19876453")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        time.sleep(1)
        driver.find_element_by_id("id_username").send_keys("usuario1")
        driver.find_element_by_id("id_passw").click()
        driver.find_element_by_id("id_passw").clear()
        time.sleep(1)
        driver.find_element_by_id("id_passw").send_keys("12345")
        driver.find_element_by_id("id_submit").click()
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        time.sleep(1)
        driver.find_element_by_name("username").send_keys("usuario1")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("12345")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        time.sleep(1)
        time.sleep(1)
        driver.find_element_by_link_text("Gestionar Instituciones").click()
        driver.find_element_by_xpath("//a[@id='add_institucion']/i").click()
        driver.find_element_by_id("id_rif").click()
        driver.find_element_by_id("id_rif").clear()
        time.sleep(1)
        driver.find_element_by_id("id_rif").send_keys("J-123456789")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        time.sleep(1)
        driver.find_element_by_id("id_name").send_keys("Institucion1")
        driver.find_element_by_id("id_address").click()
        driver.find_element_by_id("id_address").clear()
        time.sleep(1)
        driver.find_element_by_id("id_address").send_keys("Los Ruices")
        driver.find_element_by_id("id_tipo").click()
        Select(driver.find_element_by_id("id_tipo")).select_by_visible_text("Laboratorio")
        driver.find_element_by_xpath("//option[@value='Laboratorio']").click()
        driver.find_element_by_id("id_submit").click()
        time.sleep(1)
        time.sleep(1)
        driver.find_element_by_link_text("Gestionar Laboratorios").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@id='add_laboratorio']/i").click()
        driver.find_element_by_id("id_rif").click()
        driver.find_element_by_id("id_rif").clear()
        time.sleep(1)
        driver.find_element_by_id("id_rif").send_keys("J-123456786")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        time.sleep(1)
        driver.find_element_by_id("id_name").send_keys("Laboratorio Clinico")
        driver.find_element_by_id("id_address").click()
        driver.find_element_by_id("id_address").click()
        driver.find_element_by_id("id_address").clear()
        time.sleep(1)
        driver.find_element_by_id("id_address").send_keys("La Urbina")
        driver.find_element_by_id("id_regent").click()
        driver.find_element_by_id("id_regent").clear()
        time.sleep(1)
        driver.find_element_by_id("id_regent").send_keys("Carolina Perez")
        driver.find_element_by_id("id_institucion").click()
        Select(driver.find_element_by_id("id_institucion")).select_by_visible_text("Institucion1")
        driver.find_element_by_id("id_submit").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='show-laboratorios']/table/tbody/tr[2]/td[6]/a/i").click()
        time.sleep(1)
        time.sleep(1)
        driver.find_element_by_id("id_address").click()
        driver.find_element_by_id("id_address").clear()
        time.sleep(1)
        driver.find_element_by_id("id_address").send_keys("Chacao")
        driver.find_element_by_id("id_submit").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='show-laboratorios']/table/tbody/tr[2]/td[6]/a[2]/i").click()
        time.sleep(1)
        driver.find_element_by_link_text("Aceptar").click()
        time.sleep(1)
        time.sleep(1)
        driver.find_element_by_link_text("Salir").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
