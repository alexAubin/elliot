import pwd
import os
import subprocess 

class objective :


    def __init__(self, guide) :

        self.guideName        = guide.guideName
        self.traineeName      = guide.traineeName
        
        basename = "/home/"+self.traineeName+"/infectedWebsite/"

        self.basename = basename


    def title(self) :
        return "free your mind"



    def description(self) :
        return """

Comme vous commencez a le remarquer, une commande, dans l'esprit UNIX, est
une action elementaire tres simple. 

Nous allons maintenant nous deplacer dans l'arborescence avec "cd", et
editer des fichiers directement dans la console avec "nano".

Nous allons utiliser la meme arborescence "infectedWebsite" et rajouter un
fichier dedans. Avec "tree", identifiez ou se trouve le fichier "pure.css",
et creer dans le meme sous-dossier un fichier "custom.css".

 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Commandes utiles ]                                                    |
|                                                                           |
|   cd chemin/d'un/dossier        pour aller dans un autre dossier          |
|                                                                           |
|   nano nomDeFichier             pour editer un fichier (et le creer si il |
|                                 n'existe pas).                            |
|                                                                           |
 `-------------------------------------------------------------------------'

 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Objectifs ]                                                           |
|                                                                           |
|   - Creer un fichier "custom.css" dans le meme repertoire que "pure.css"  |
|                                                                           |
|   - Le fichier "custom.css" doit contenir "I am not empty"                |
|                                                                           |
 `-------------------------------------------------------------------------'

N'oubliez pas que vous pouvez utiliser <Tab> pour autocompleter des noms de
fichiers ou dossiers, et <Haut> pour retrouver les commandes que vous avez 
taper precedemment.

Une fois que vous avez termine, envoyez-moi un mail vide avec

  mail """+self.guideName+"""
		"""



    def sorry(self) :
        return """
Desole, il semblerait que vous n'ayez pas encore cree le fichier "custom.css" 
dans le meme sous-dossier que "pure.css", ou bien le fichier ne contiennent pas
la phrase "I am not empty".
  
"""	


    def checkIfComplete(self) :

        p1 = subprocess.Popen(["cat",  self.basename+"/css/custom.css" ],    stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "I am not empty" ],  stdin=p1.stdout, stdout=subprocess.PIPE)
        output = p2.communicate()[0]

        if (output != "") :
            return True;
        else :
            return False;


