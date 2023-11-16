
from src.python.application.environment.BuildEnvironment import buildEnvironment
from src.python.application.environment.Environment import Environment


class MimicBot:
    def __init__(self, commandPrefix="!"):
        buildEnvironment()
        self.environment = Environment.load()



    def run(self):
        print(f"Run")
