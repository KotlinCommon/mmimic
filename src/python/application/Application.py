import sys
sys = sys.path.append('/app/src/python/')
from src.python.domain.MimicBot import MimicBot

if __name__ == "__main__":
    bot = MimicBot()
    bot.run()
