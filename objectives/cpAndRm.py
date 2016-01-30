import pwd
import os
import subprocess 

class objective :


    def __init__(self, guide) :

        self.guideName        = guide.guideName
        self.traineeName      = guide.traineeName
        
        basename = "/home/"+self.guideName

        self.mkdir(basename            )
        self.mkdir(basename+"/scripts/")
        self.touch(basename+"/scripts/fsociety00.dat"	)

        with open(basename+"/scripts/fsociety00.dat",'w') as f :
            f.write("###   I wanted to save the world.  \n")


    def mkdir(self,foldername) :
	try :
		os.makedirs(foldername)
	except OSError :
		pass

        # Dirty hack
        gid = pwd.getpwnam(self.traineeName).pw_uid
        uid = pwd.getpwnam(self.guideName).pw_uid
        os.chown(foldername,uid,gid) 



    def touch(self,filename) :
        open(filename, 'a').close()
 
        # Dirty hack
        gid = pwd.getpwnam(self.traineeName).pw_uid
        uid = pwd.getpwnam(self.guideName).pw_uid
        os.chown(filename,uid,gid) 

       


    def title(self) :
        return "fsociety00.dat"



    def description(self) :
        return """
Okay.

Vous commencez a comprendre le principe.

Nous devons apporter quelques autres modifications a l'arborescence de
"infectedWebsite.". Il vous faut remplacer le fichier "facebook00.dat" par le
fichier "fsociety00.dat" qui se trouve dans le dossier "scripts" dans mon home.

 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Commandes utiles ]                                                    |
|                                                                           |
|   rm chemin/du/fichier          pour effacer un fichier                   |
|                                                                           |
|   cp fichier destination        pour copier un fichier d'une source a     |
|                                 une destination                           |
|                                                                           |
 `-------------------------------------------------------------------------'
                                                                           
 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Objectifs ]                                                           |
|                                                                           |
|   - Localiser le fichier "fsociety00.dat" dans mon $HOME                  |
|                                                                           |
|   - Remplacer le fichier facebook00.dat dans "infectedWebsite" par le     |
|     fichier "fsociety00.dat"                                              |
|                                                                           |
 `-------------------------------------------------------------------------'

Une fois que vous avez termine, envoyez-moi un mail vide avec

  mail """+self.guideName+"""
		"""



    def sorry(self) :
        return """
Desole, il semblerait que vous n'ayez pas encore supprimer le fichier "facebook00.dat" et que le fichier "fsociety00.dat" ne soit pas encore la.
"""	


    def checkIfComplete(self) :
	
	basename = "/home/"+self.traineeName+"/infectedWebsite"

	facebookFlag = os.path.isfile(basename+"/scripts/facebook00.dat")
	fsocietyFlag = os.path.isfile(basename+"/scripts/fsociety00.dat")

	if ((not facebookFlag) and (fsocietyFlag)) :
            return True;
        else :
            return False;


