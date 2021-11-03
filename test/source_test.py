import unittest
from app.models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('blasting-news-br','Blasting News (BR)','Descubra a seção brasileira da Blasting News, a primeira revista feita pelo  público, com notícias globais e vídeos independentes. Junte-se a nós e torne- se um repórter.','https://br.blastingnews.com','general','br','pt')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
    def test_to_check_instance_variables(self):
        self.assertEqual(self.new_source.id,'blasting-news-br')
        self.assertEqual(self.new_source.name,'Blasting News (BR)')
        self.assertEqual(self.new_source.description,'BDescubra a seção brasileira da Blasting News, a primeira revista feita pelo  público, com notícias globais e vídeos independentes. Junte-se a nós e torne- se um repórter.')
        self.assertEqual(self.new_source.url,'https://br.blastingnews.com')
        self.assertEqual(self.new_source.category,'general')
        self.assertEqual(self.new_source.country,'br')
        self.assertEqual(self.new_source.language,'pt')


if __name__ == '__main__':
    unittest.main()