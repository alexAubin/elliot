import pwd
import os
import subprocess 

class objective :


    def __init__(self, guide) :

        self.guideName        = guide.guideName
        self.traineeName      = guide.traineeName


    

    def title(self) :
        return "system breach"



    def description(self) :
        return """
Dans cette derniere partie, nous allons decouvrir le gestionnaire de paquet.

Avec toute distribution GNU/Linux viens generalement un gestionnaire de
paquet. C'est un programme qui permet de telecharger d'autres programmes : pas
besoin de trouver un site web qui permet de telecharger un installeur. Le
gestionnaire de paquet sans passer par un intermediaire. Il s'occupe egalement
d'installer tout le necessaire (dependances), et de mettre a jour de facon
unifiee tous les programmes installes.

(N.B. : dans la vraie vie, le gestionnaire de paquet peut aussi s'utiliser en
interface graphique)

 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Commandes utiles ]                                                    |
|                                                                           |
|   sudo commande      Execute une commande avec les droits root (c'est a   |
|                      dire administrateur). En particulier, apt-get        |
|                      necessite d'etre execute avec "sudo" car installer   |
|                      de nouveaux programmes de mettre a jour le systeme   |
|                      releve de l'administration.                          |
|                                                                           |
|   apt-get update     Questionne les depots de logiciels pour demander si  |
|                      des mises a jour sont disponibles                    |
|                                                                           |
|   apt-get upgrade    Lance la mise a jour de tous les programmes qui ont  |
|                      ete installe via le gestionnaire de paquet           |
|                                                                           |
|   apt-cache search paquet    Cherche si un paquet existe                  |
|                                                                           |
|   apt-get install paquet     Demande d'installer un paquet                |
|                                                                           |
 `-------------------------------------------------------------------------'
                                                                           
 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Objectifs ]                                                           |
|                                                                           |
|   - Mettre a jour votre systeme (update et upgrade)                       |
|                                                                           |
|   - Demander si le paquet "links" existe                                  | 
|                                                                           |
|   - Installer "links"                                                     | 
|                                                                           |
|   - Essayer la commande "links fr.wikipedia.org"                          | 
|                                                                           |
 `-------------------------------------------------------------------------'

Une fois que vous avez termine, envoyez-moi un mail vide avec

  mail """+self.guideName+"""
        """



    def sorry(self) :
        return """
Desole, links n'est pas encore installe sur le systeme.
"""    


    def checkIfComplete(self) :
	
	flag = os.path.isfile("/usr/bin/links")

        return flag;


