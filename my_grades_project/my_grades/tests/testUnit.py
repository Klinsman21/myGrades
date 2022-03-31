from django.test import TestCase
from django.test import Client
from ..models import *

class ModelUsuarioTeste(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Usuario.objects.create(username='Klinsman', password='12345678',
                               matricula='0088', email='test@example.com'
                               )

    def test_matricula_usuario_comecando_com_zero(self):
        user = Usuario.objects.get(email='test@example.com')
        matricula = user.matricula
        resultado = matricula.startswith("0")
        self.assertTrue(resultado)

    def test_tipo_usuario_sendo_salvo_como_numerico(self):
        user=Usuario.objects.get(email='test@example.com')
        userType = user.tipoUsuario
        self.assertEquals(userType + 0, userType)

    def test_o_primeiro_nome_do_usuario_foi_inserido(self):
        user = Usuario.objects.get(email='test@example.com')
        first_name_length = len(user.first_name) 
        resultado = first_name_length > 0
        self.assertTrue(resultado)

    def test_o_usuario_e_professor(self):
        # para o teste se o tipoUsuario for 1 o usuário é um aulo se for 2 é professor
        user = Usuario.objects.get(email='test@example.com')
        self.assertEquals(user.tipoUsuario, 2)

    def test_usuario_e_superuser(self):
        emails = Usuario.objects.filter(is_superuser=True).values_list('email')
        resultado = 'test@example.com' in emails
        self.assertTrue(resultado)
        
        

class TestandoViews(TestCase):
    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods
        Usuario.objects.create(username='Klinsman', password='12345678',
                               matricula='0088', email='test@example.com'
                               )
        
        Usuario.objects.create(username='Josy', password='12345678',
                               matricula='7766', email='test2@example.com'
                               )
            
        Disciplina.objects.create(nome='Testes de software')
        disciplina = Disciplina.objects.get(nome='Testes de software')
        aluno = Usuario.objects.get(matricula='7766')
        
        Nota.objects.create(disciplina=disciplina, aluno=aluno, periodo=2, nota=70, tipo='Prova')
        Nota.objects.create(disciplina=disciplina, aluno=aluno, periodo=1, nota=90, tipo='Artigo')
        Nota.objects.create(disciplina=disciplina, aluno=aluno, periodo=2, nota=60, tipo='Trabalho')
        Nota.objects.create(disciplina=disciplina, aluno=aluno, periodo=2, nota=70, tipo='Prova')
        
        c = Client()
        self.client = c.login(matricula='7766', password='12345678')

    def test_notas_atribuidas_ao_aluno(self):
       response = self.client.get('/painel')
       self.assertEqual(response.status_code, 200)

    def test_verificando_se_a_view_listaNotas_retorna_as_notas_do_segundo_periodo(self):
        response = self.client.get('/notas/2/')
        self.assertTrue(len(response.context['nota']) > 0)

    def test_acesso_area_de_cadastro_de_aluno(self):
        response = self.client.get('/cadastro')
        self.assertEqual(response.status_code, 200)
        
    def test_deletar_endereco_que_nao_existe(self):
        response = self.client.get('/deletarEndereco/3/')
        self.assertEqual(response.status_code, 200)
        
    def test_verificando_se_a_view_cadastro_esta_renderizando_o_html_correto(self):
        response = self.client.get('/cadastro')
        self.assertTemplateUsed(response, 'my_grades/cadastro.html')
