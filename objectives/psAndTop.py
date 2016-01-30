import pwd
import os
import subprocess 

class objective :


    def __init__(self, guide) :

        self.guideName        = guide.guideName
        self.traineeName      = guide.traineeName

        basename = "/home/"+self.guideName

        with open(basename+"/evilCode.sh",'w') as f :
            f.write("#!/bin/bash     \n")
            f.write(" \n")
            f.write("while true\n")
            f.write("do\n")
            f.write("    echo 'I am a script that does evil things !!!'\n")
            f.write("                                 # Such as stealing CPU !\n")
            f.write("    for i in `seq 1 10000`; do echo $((42**42))>/dev/null; done\n") 
            f.write("    sleep 2                      # And sleeping !\n")
            f.write("done\n")
            os.chmod(basename+"/evilCode.sh", 0777)
            #os.stat.S_IXOTH)

        cmd =   "su -m "+self.traineeName+" -c "+basename+"/evilCode.sh"
        
        self.evilProcess = subprocess.Popen([cmd], shell=True,
                       stdin=None, stdout=None, stderr=None, close_fds=True)


    

    def title(self) :
        return "e-corp"



    def description(self) :
        return """
Bien joue!

Vous commencez a connaitre quelques commandes et a savoir comment manipuler des
fichiers. Regardons maintenant du cote des processus.

J'ai lance un programme qui s'apelle "evilCode.sh", votre objectif est de
l'arreter. Comme tous les processus, il dispose d'un identifiant (PID), d'un
processus parent (PPID), et d'un proprietaire. (Pour cet exercice, vous etes le
proprietaire du programme "evilCode.sh".)

 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Commandes utiles ]                                                    |
|                                                                           |
|   top                lister en temps reel les processus qui tournent et   |
|                      leur utilisation en terme de calcul (CPU) et de      |
|                      memoire vive (MEM). (Quittez avec 'q')               |
|                                                                           |
|   ps -A --forest     lister tous les processus qui tournent actuellement  |
|                                                                           |
|   ps -u futurenerd   lister tous les processus qui vous appartiennent     |
|                                                                           |
|   kill -9 numero     tue le processus a partir de son identifiant (PID)   |
|                                                                           |
 `-------------------------------------------------------------------------'
                                                                           
 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Objectifs ]                                                           |
|                                                                           |
|   - Etudier l'ensemble des processus qui tournent sur la machine avec     |
|        ps -A --forest                                                     | 
|     qui affiche les processus sous forme d'arborescence                   |
|     en particulier, les processus fils de kthreadd corresponds au noyau   |
|     Linux.                                                                |
|                                                                           |
|   - Lancer "top" et regarder si "evilCode.sh" est present                 |
|                                                                           |
|   - Trouver le PID du processus "evilCode.sh", soit avec "top", soit en   |
|     s'aidant de grep :                                                    |
|         ps -u futurenerd | grep "evil"                                    |
|                                                                           |
|   - Tuez le processus "evilCode.sh"                                       |
|                                                                           |
 `-------------------------------------------------------------------------'

Une fois que vous avez termine, envoyez-moi un mail vide avec

  mail """+self.guideName+"""
        """



    def sorry(self) :
        return """
Desole, il semblerait que le processus evilCode.sh soit encore en train de tourner.
"""    


    def checkIfComplete(self) :

        if (self.evilProcess.poll() != None) :
            return True;
        else :
            return False;


