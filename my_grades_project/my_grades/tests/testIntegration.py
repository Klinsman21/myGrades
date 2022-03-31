from django.test import RequestFactory, TestCase, Client
from ..views import ControlPainel, EnderecoLista

from ..models import *



class IntegracaoComAPINode(TestCase):
    @classmethod
    
    def setUpTestData(self):
        c = Client()
        self.client = c.login(matricula='0000', password='12345678')
    
    # A view ControlPainel faz a integração com o banco redis
    def test_integracao_com_banco_redis_verificando_se_os_dados_de_avisos_foram_recuperados(self):
        request = RequestFactory().get('/painel')
        view = ControlPainel()
        view.setup(request)
        
        context = view.get_context_data()
        self.assertTrue(len(context['avisos']) > 0)
        
    # A view  faz a integração com o banco mongoDB
    def test_integracao_com_banco_mongoDB_verificando_se_a_latitude_e_longitude_foram_recuperados(self):
        request = RequestFactory().get('/enderecoLista')
        view = EnderecoLista()
        view.setup(request)
        
        context = view.get_context_data()
        self.assertTrue(len(context['latlng']) > 0)
