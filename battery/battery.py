from abc import abstractmethod


class Battery:
    @abstractmethod
    def needs_service(self):
        pass