

from abc import ABC, abstractclassmethod, abstractmethod, abstractstaticmethod


class MetaMail(ABC):

    @classmethod
    def __subclasshook__(cls,subclass):
        return(
            hasattr(subclass,"SendMessage")and callable(subclass.SendMessage) and
            hasattr(subclass,"CreateMessage")and callable(subclass.CreateMessage)

        )

    @abstractmethod
    def CreateMessage(self,sender:str,receiver:str,message:str="")->dict:

        """Creates a formated email message with a sender:str , a receiver:str  and a message body adn returns it as a dict(dict)"""

        raise NotImplementedError    

    @abstractmethod
    def SendMessage(self,message:dict,password:str)->bool:

        """Send email message once all the parameters are properly configured
        returns true if the email was successfully sent"""

        raise NotImplementedError

    @abstractstaticmethod
    def GetInstance(self):
        """Returns the mail service instance"""

        raise NotImplementedError