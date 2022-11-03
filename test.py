class Singleton:
    __sync_source_map = None
    __integration_onboarding_map = None

    @staticmethod
    def getInstance(org_id):
        """ Static access method. """
        if Singleton.__sync_source_map == None:
            Singleton(org_id)
        return Singleton.__sync_source_map

    @staticmethod
    def calc(org_id):
        return {'org_id':org_id}

    def __init__(self,data):
          """ Virtually private constructor. """
          if Singleton.__sync_source_map != None:
             raise Exception("This class is a singleton!")
          else:
             Singleton.__sync_source_map = {'data':Singleton.calc(data)}

s = Singleton(12)
print(s)

s = Singleton.getInstance(123)
print(s)

s = Singleton.getInstance(11)
print(s)