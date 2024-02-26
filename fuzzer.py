from config import TreeConfig, GlobalConfig
from document import Document
from utils.random import Random

import os
import time
import pickle
from enum import Enum


class Fuzzer:
    def __init__(self, executor, manager):
        super().__init__()
        self.manager = manager
        self.executor = executor
        self.start_time = time.time()

    def generate_one(self):
        document = Document(Random.range(TreeConfig.min_element_count, TreeConfig.max_element_count))
        document.generate_nodes()
        document.generate_attributes()
        document.generate_css_rules()
        # document.generate_js_functions()
        return document
    
    #Implemented by STARLab
    def mutate_one(self, document:Document):
        #Text Mutation
        document.dom_tree.mutate_text()
        #Class Addition
        document.dom_tree.insert_class()
        #CSS rule Addition
        document.css.insert_rule(document.dom_tree.element_count)
        return document

    def generate_only(self, num):
        for i in range(num):
            print("Generating testcase #{}".format(i))
            document = self.generate_one()
            self.manager.save_testcase(document, "original")
            document = self.mutate_one(document)
            self.manager.save_testcase(document, "mutated")
            self.manager.count += 1
            
        print("Total {} testcases have been written to '{}'".format(num, os.path.abspath(self.manager.output_dir)))

