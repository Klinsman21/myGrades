from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TesteLogin(LiveServerTestCase):

  def test_fazendo_login_no_sistema(self):
    selenium = webdriver.Chrome()
    selenium.get('http://127.0.0.1:8000/')

    matricula = selenium.find_element_by_id('id_matricula')
    password = selenium.find_element_by_id('id_password')
    
    submit = selenium.find_element_by_id('submit_button')

    matricula.send_keys('0000')
    password.send_keys('12345678')

    #submit form
    submit.send_keys(Keys.RETURN)

    assert 'Klinsman' in selenium.page_source
    
def test_acessando_painel_de_controle(self):
    selenium = webdriver.Chrome()
    selenium.get('http://127.0.0.1:8000/painel')

    assert 'painel de controle' in selenium.page_source