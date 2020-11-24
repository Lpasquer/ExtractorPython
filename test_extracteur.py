import unittest
from urllib.request import urlopen
from extracteur import*


class TestExtracteur(unittest.TestCase):
        
    def test_recup_liste_url(self):#test pour la fonction qui recup la liste des url
        urls = "wikiurls.txt"
        list_url=recup_liste_url(urls)   
        self.assertEqual(len(list_url),336)#336 url dans le fichier
    
    def test_recup_tableau(self):#test pour la fonction qui recupere les tableaux
        url='https://en.wikipedia.org/wiki/New_York_City'
        tableau=recup_tableau(url)
        self.assertTrue(tableau)
        self.assertEqual(len(tableau),7)#7 tableaux dans la page

    def test_get_table_rows(self):#test pour la fonction qui recupere les info du tableau et qui les tries
        url='https://en.wikipedia.org/wiki/New_York_City'
        tables = recup_tableau(url)
        if tables is not None:
            table=tables[0]
            rows = get_table_rows(table)
            self.assertEqual(len(rows),11)#11 lignes dans le premier tableau de la page

    def test_wikipedia_extractor_save_to_csv(self):#test pour la fonction qui créé les fichier csv
        #et pour la fonction qui converti notre variable rows en dataframe
        url='https://en.wikipedia.org/wiki/New_York_City'
        wikipedia_extractor(url) #on verifie que tous les csv sont créés
        self.assertTrue(os.path.isfile("output/New_York_City_1.csv"))
        self.assertTrue(os.path.isfile("output/New_York_City_2.csv"))
        self.assertTrue(os.path.isfile("output/New_York_City_3.csv"))
        self.assertTrue(os.path.isfile("output/New_York_City_4.csv"))
        self.assertTrue(os.path.isfile("output/New_York_City_5.csv"))
        self.assertTrue(os.path.isfile("output/New_York_City_6.csv"))
        self.assertTrue(os.path.isfile("output/New_York_City_7.csv"))
        
        df = pd.read_csv('output/New_York_City_1.csv')#on verifie qu'il y ale bon nb de lignes et de colonnes dans le fichier
        self.assertEqual(df.shape,(11,10))#df.shape donne un tuple de type(nb ligne,nb colonne) du csv
        #11 est le nombre de ligne du tableau et 10 le nb de colonnes
        
if __name__ == '__main__':
    unittest.main()


