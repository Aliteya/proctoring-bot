from configparser import ConfigParser


class BaseConfigurator:
    def __init__(self, config_file: str):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_bot_option(self, option: str) -> str:
        return self.config["Bot"][option]

    def get_chat_option(self, option: str) -> str:
        return self.config["Chat"][option]

    def get_spreadsheet_option(self, option: str) -> str:
        return self.config["Spreadsheet"][option]
