#!/usr/bin/env python
import json

class Config:
    def __init__(self, name='config'):
        self.name = name
        self.config = None

    def get_config(self):
        if self.config is None:
            f = open(self.name +'.json', 'r')
            self.config = json.load(f)
            f.close()
        return self.config