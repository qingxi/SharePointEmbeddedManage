ContainerTypeId = '<CONTAINER TYPE ID>';

class Config:
    def __init__(self):
        self._containerId = '<DEFAULT CONTAINER ID>';
    def setContainerId(self, _containerId):
        self._containerId = _containerId;

    def getContainerId(self):
        return self._containerId;