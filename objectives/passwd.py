
import subprocess 

class objective :


    def __init__(self, guide) :

        self.guideName        = guide.guideName
        self.traineeName      = guide.traineeName
        
        self.initPasswordHash = self.getPasswordHash()


    def title(self) :
        return "hello friend"



    def description(self) :
        return """

Bienvenue dans ce tutorial.

Avant de commencer, nous devons prendre quelques precautions.

Les autres participants connaissent votre mot de passe et peuvent prendre le
controle de votre machine a tout moment.  Votre premier objectif est de changer
votre mot de passe.

 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Commandes utiles ]                                                    |
|                                                                           |
|   passwd                                                                  |
|                                                                           |
 `-------------------------------------------------------------------------'
                                                                           
 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Objectifs ]                                                           |
|                                                                           |
|   Changer votre mot de passe avec passwd                                  |
|                                                                           |
 `-------------------------------------------------------------------------'

Une fois que vous avez termine, envoyez-moi un mail vide avec

  mail """+self.guideName+"""
        """



    def sorry(self) :
        return """
Desole, il semblerait que vous n'ayez pas encore change votre mot de passe.

Vous devez taper

  passwd

dans votre console, puis choisir un nouveau mot de passe.

"""    



    def getPasswordHash(self) :

        p1 = subprocess.Popen(["cat", "/etc/shadow"     ],                   stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", self.traineeName ],  stdin=p1.stdout, stdout=subprocess.PIPE)
        p3 = subprocess.Popen(["tr",   "':'", "' '"     ],  stdin=p2.stdout, stdout=subprocess.PIPE)
        p4 = subprocess.Popen(["awk",  "{print $2}"     ],  stdin=p3.stdout, stdout=subprocess.PIPE)
        output = p4.communicate()[0]

        return output



    def checkIfComplete(self) :

        if (self.initPasswordHash != self.getPasswordHash()) :
            return True;
        else :
            return False;


