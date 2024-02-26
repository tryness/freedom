from utils.random import random

import os
import time
import pickle
import shutil
import fnmatch

#Modified by STARLab
class Manager:
    def __init__(self, index, generate_only, output_dir=None):
        self.generate_only = generate_only
        self.index = index
        self.count = 0

        if generate_only:
            if os.path.exists(output_dir):
                shutil.rmtree(output_dir)
            os.mkdir(output_dir)
            self.output_dir = output_dir
        else:
            pass

    def fn(self):
        # return "{}-{}".format(self.index, int(time.time() * 100))
        return f"fuzz_{self.count:0>6}"
    
    #Modified by STARLab
    def save_testcase(self, document, name, cov=None):
        if self.generate_only:
            path = os.path.join(self.output_dir, "{}_{}.html".format(self.fn(), name))
            with open(path, "w") as f:
                f.write(str(document))
        else:
            pass
