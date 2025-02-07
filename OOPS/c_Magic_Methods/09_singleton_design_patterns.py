class Singleton(object):
    __singleton = None

    def __new__(cls,*args, **kwargs):
        if not cls.__singleton :
            cls.__singleton = super().__new__(cls,*args, **kwargs)
        return cls.__singleton
        
    # def __new__(cls, *args, **kwargs): another way writting for above code
    #     if cls.__singleton is None:
    #         # Create the instance only if it doesn't exist
    #         cls.__singleton = super().__new__(cls, *args, **kwargs)
    #     return cls.__singleton  # Always return the same instance

class Myclass(Singleton):
    def __init__(self) -> None:
        super().__init__()

if __name__ == "__main__":
    c1 = Myclass()
    print(f"{c1         =}")
    print(c1)

    c2 = Myclass()
    print(f"{c2         =}")

    print(id(c1)    ==  id(c2))
    assert c1 == c2