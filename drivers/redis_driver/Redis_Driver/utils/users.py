from redis import Redis
from typing import List,NewType

class Users:
    """Contains commands related with the management of users 
    and thier access to resources within the Redis server like:
        - users_list : Returns a list with the current users
        - add_user : Adds a new user to the database and grants permissions
        -
    """
    stringlist=NewType("list[str]",List[str])
    def __init__(self,r:Redis) -> None:
        self.__r=r 

        
    def close(self):
        self.__r.quit()
        self.__r=None


    def users_list(self)->list:
        return self.__r.acl_list()

    def add_user(self,username:str,
    enabled:bool,
    password:str,
    nopass:bool=False,
    categories:stringlist=None,
    commands:stringlist=None,
    keys:stringlist=None
    ):
        """Adds a new user to the database and grants permissions.
        There are three types of permisions that can be granted.
            - category : category commands the user can execute. This is usefull
            if you want to give access to a bunch of commands with just one word.
            - commands : commands the user can execute.
            - keys : keys to which the user has access.
        
        Args:
            - username (str): Name/alias of the user
            - enabled (bool): True if the user is to be actiavated. False if the user is to be blocked/disabled.
            - password (str): User password
            - nopass (bool, optional): True if the user requires no password. Defaults to False.
            - categories (stringlist, optional): List of categories the give access to a group of commands. Defaults to None.
            The format of each item must be a string like : "+category_x".
            - commands (stringlist, optional): List of commands the user will have access to. Defaults to None.
            - keys (stringlist, optional): List of keys the user will have access to. Defaults to None.
            ---
            Example :
                categories = ["+write","+read"] will give access to the user to all the commands 
                that fall in the category write and read. Use categories_list() to check the 
                commands that fall in each category. "*" allows access to all categories.
            ---
            Example:
                commands = ["+set","+mset","+get"] will give access to the user to the commands 
                set ,mset and get . "*" allow access to all commands.
            ---
            Example:
                keys = ["key_name*","other_key_name:*","somekey_*"] will give access to 
                - keys that start with : key_name
                - keys that start with : other_key_name:
                - keys that start with : somekey_
                \n
            `Using only "*" will grant access to all keys`

                
        """
        self.__r.acl_setuser(
            username=username,
            enabled=enabled,
            nopass=nopass,
            passwords=password,
            categories=categories,
            commands=commands,
            keys=keys
            )


    def categories_list(self,category:str=None)->stringlist:
        """Returns the list of command categories available
        List of categories : 
        1) "keyspace"
        2) "read"
        3) "write"
        4) "set"
        5) "sortedset"
        6) "list"
        7) "hash"
        8) "string"
        9) "bitmap"
        10) "hyperloglog"
        11) "geo"
        12) "stream"
        13) "pubsub"
        14) "admin"
        15) "fast"
        16) "slow"
        17) "blocking"
        18) "dangerous"
        19) "connection"
        20) "transaction"
        21) "scripting"
        
        `You can find information about each category at : https://redis.io/docs/manual/security/acl/ `
        Args:
            category (str, optional): category. Defaults to None.
        """
        return self.__r.acl_cat(category=category)



    