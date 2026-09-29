from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass

class LocalStorage(Storage):
    def save(self, data):
        return f"Saved locally: {data}"

class CloudStorage(Storage):
    def save(self, data):
        return f"Saved to cloud: {data}"

def backup(storage, data):
    print(storage.save(data))

backup(LocalStorage(), "assignment.py")
backup(CloudStorage(), "notes.pdf")
