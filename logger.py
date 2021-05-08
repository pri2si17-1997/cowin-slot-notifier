class Logger:
    def __init__(self, stdout):
        self.terminal = stdout
        self.log = open("vaccine_slots.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        pass