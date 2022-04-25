import yaml


class Configuration:
    def __init__(self, config_file: str):
        self.config = Configuration.load(config_file)
        self.set_attrs()

    @staticmethod
    def load(config_file: str) -> dict:
        with open(config_file) as _log_file:
            config = yaml.safe_load(_log_file)
        return config

    def set_attrs(self):
        for k, v in self.config.items():
            setattr(self, k, v)
