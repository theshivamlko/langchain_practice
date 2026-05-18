
from  configparser import ConfigParser


class Config:
    def __init__(self,config_file='./src/langgraphai/ui/uiconfig.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        llm_options = self.config['DEFAULT'].get('LLM_OPTIONS', '').split(',')
        return llm_options

    def get_usecase_options(self):
        usecase_options = self.config['DEFAULT'].get('USECASE_OPTIONS', '').split(',')
        return usecase_options

    def get_models_options(self):
        models = self.config['DEFAULT'].get('MODELS_OPTIONS', '').split(',')
        return models

    def get_page_title(self):
        page_title = self.config['DEFAULT'].get('PAGE_TITLE', '')
        return page_title


