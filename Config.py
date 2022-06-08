import configparser


class Config:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config/app.ini')

    def get(self, section, name):
        value = self.config[section][name]
        if value.isnumeric():
            value = int(value)
        return value
