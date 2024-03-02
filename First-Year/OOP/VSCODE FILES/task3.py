class GameManager:
    singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = \
                super(GameManager, cls).__new__(cls, *args, **kwargs)
        return cls.singleton
    def __eq__(self,object):
        if id(self)==id(object):
            print("We are the same object because we have the same object ID!")
            return True
        else:
            print("We are not the same object!")
            return False

g1 = GameManager()
g2 = GameManager()
g1==g2
