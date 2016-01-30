import pwd
import os
import subprocess 

class objective :


    def __init__(self, guide) :

        self.guideName        = guide.guideName
        self.traineeName      = guide.traineeName


    

    def title(self) :
        return "congratz"



    def description(self) :
        return """
Felicitation, vous avez termine tous les objectifs de cette partie !

 ,-------------------------------------------------------------------------,
|                                                                           |
|   [ Credits ]                                                             |
|                                                                           |
|   Alex      -- Main dev                                                   |
|                                                                           |
|   Akaash    -- Beta-testeur, UX designer                                  |
|                                                                           |
|   Nico      -- Beta-testeur, UX designer                                  |
|                                                                           |
|   Odile     -- Beta-testeuse                                              |
|                                                                           |
 `-------------------------------------------------------------------------'

        """


    def sorry(self) :
        return """
"""    


    def checkIfComplete(self) :

        return True


