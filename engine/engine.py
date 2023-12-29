from abc import abstractmethod


class Engine:
    @abstractmethod
    def needs_service(self):
        pass