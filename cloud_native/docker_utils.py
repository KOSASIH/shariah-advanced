import docker

class DockerUtils:
    def __init__(self):
        self.client = docker.from_env()

    def create_container(self, image, command):
        container = self.client.containers.create(image, command)
        return container

    def start_container(self, container):
        container.start()

    def stop_container(self, container):
        container.stop()
