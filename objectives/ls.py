import pwd
import os
import subprocess 

class objective :


    def __init__(self, guide) :

        self.guideName        = guide.guideName
        self.traineeName      = guide.traineeName
        
        basename = "/home/"+self.traineeName+"/infectedWebsite/"

        self.mkdir(basename            )
        self.mkdir(basename+"/css/"    )
        self.mkdir(basename+"/scripts/")
        self.mkdir(basename+"/images/" )
        self.mkdir(basename+"/db/"     )
        self.touch(basename+"/index.html"		)
        self.touch(basename+"/css/style.css"		)
        self.touch(basename+"/css/pure.css"		)
        self.touch(basename+"/scripts/facebook00.dat"   )
        self.touch(basename+"/images/cuteKittens.jpg"	)
        self.touch(basename+"/images/majesticFloof.jpg"	)
        self.touch(basename+"/images/evilBunny.jpg"	)
        self.touch(basename+"/db/users.db"		)
        self.touch(basename+"/db/logs.db"		)

        self.basename = basename


    def mkdir(self,foldername) :
	try :
		os.makedirs(foldername)
	except OSError :
		pass

        # Dirty hack
        uid = pwd.getpwnam(self.traineeName).pw_uid
        gid = pwd.getpwnam(self.guideName).pw_uid
        os.chown(foldername,uid,gid) 


    def touch(self,filename) :
        open(filename, 'a').close()
 
        # Dirty hack
        uid = pwd.getpwnam(self.traineeName).pw_uid
        gid = pwd.getpwnam(self.guideName).pw_uid
        os.chown(filename,uid,gid) 

       


    def title(self) :
        return "follow the white rabbit"



    def description(self) :
        return """
Felicitations, vous avez change votre mot de passe !

Le prochain objectif est destine a vous faire prendre en main la ligne de
commande.

J'ai cree une arborescence de fichier dans votre $HOME, dans un dossier qui
s'appelle "infectedWebsite". Votre objectif pour le moment est simplement
d'inspecter le contenu de ce dossier. 

 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Commandes utiles ]                                                    |
|                                                                           |
|   pwd               dire ou vous etes                                     |
|                                                                           |
|   ls                pour lister le contenu du dossier dans lequel vous    |
|                     etes                                                  |
|                                                                           |
|   ls dossier        pour lister le contenu d'un autre dossier             |
|                                                                           |
|   ls -l dossier     pour avoir des informations detaille                  |
|                                                                           |
|   tree dossier      pour afficher sous forme d'arbre l'arborescence d'un  |
|                     dossier                                               |
|                                                                           |
 `-------------------------------------------------------------------------'

 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Objectifs ]                                                           |
|                                                                           |
|   - Verifier que vous etes dans votre $HOME avec la commande "pwd"        |
|                                                                           |
|   - Lister le contenu de votre $HOME, puis de "infectedWebsite"           |
|                                                                           |
|   - Creer un alias pour que lorsque vous tapez "ll", cela execute "ls -l" |
|     Pour ce faire, taper : alias ll='ls -l'                               |
|                                                                           |
 `-------------------------------------------------------------------------'

N'oubliez pas que vous pouvez utiliser <Tab> pour autocompleter des noms de
fichiers ou dossiers, et <Haut> pour retrouver les commandes que vous avez 
tape precedemment.

Une fois que vous avez termine, envoyez-moi un mail vide avec

  mail """+self.guideName+"""
		"""



    def sorry(self) :
        return ""	


    def checkIfComplete(self) :

        return True;


