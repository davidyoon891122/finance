import yaml


class Config():
    def __init__(self, yaml_path=None):
        self.yaml_path = yaml_path
        self.fallback = None
        
        if yaml_path:
            try:
                with open(self.yaml_path, 'r') as f:
                    self.fallback = yaml.safe_load(f)
            except: 
                pass

        if not self.fallback:
            self.fallback = {}


