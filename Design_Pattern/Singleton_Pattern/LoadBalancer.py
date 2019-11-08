import random

class LoadBalancer():
    """
    The reason why __serverList isn't private static 
    is that each Balancer object should know the servers!
    """
    __instance = None
    def __init__(self):        
        self.__serverList = []

    @staticmethod
    def getLoadBalancer():
        if LoadBalancer.__instance == None:
            LoadBalancer.__instance = LoadBalancer()
        return LoadBalancer.__instance

    def addServer(self, server):
        self.__serverList.append(server)

    def removeServer(self, server):
        self.__serverList.remove(server)

    def getServer(self):
        return self.__serverList[random.randint(0, len(self.__serverList)-1)]


class Client():
    def __init__(self):
        pass

    @staticmethod
    def test():
        balancer1 = LoadBalancer().getLoadBalancer()
        balancer2 = LoadBalancer().getLoadBalancer()
        balancer3 = LoadBalancer().getLoadBalancer()
        balancer4 = LoadBalancer().getLoadBalancer()

        # judge whether the balancers are the same one or not
        if balancer1 == balancer2 and balancer2 == balancer3 and balancer3 == balancer4:
            print("The Sever Balancer is single!")
        
        # add servers
        balancer1.addServer("Server 1")
        balancer2.addServer("Server 2")
        balancer3.addServer("Server 3")
        balancer4.addServer("Server 4")
        
        for i in range(10):
            server = balancer1.getServer()
            print("sending message to ", server)

if __name__ ==  "__main__":
    client = Client()
    client.test()
