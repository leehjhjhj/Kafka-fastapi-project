from abc import abstractmethod, ABC

class Consumer(ABC):
    @abstractmethod
    async def start(self):
        pass
    
    @abstractmethod
    async def stop(self):
        pass

    @abstractmethod
    async def consume(self):
        pass