import numpy as np, matplotlib.pyplot as plt
import sys, os, time


class FunctionGenerator:
    TYPE = ''
    SIZE = 0
    A = 0
    quantities = ['numeric', 'visual', 'text']
    operations = ['+', '-', '*', '/']

    def __init__(self, nsamples, form):
        self.SIZE = nsamples
        if form in self.quantities:
            self.TYPE = form

    def set_numeric(self):
        # Add parameters
        params = {}
        # Define relationship of each
        operations = []
        # Generate function and evaluate

    def set_visual(self):
        basis = -1
        op_mode = -1
        width = int(input('Enter width: '))
        height = int(input('Enter height: '))

        choices = 'Possible ImageFunction Types:' \
                  '[1] Static Seed Image Operations' \
                  '[2] Generative Image Operation' \
                  '[3] Generative Operations on Image Seeds'
        print choices
        variety = int(input('Enter a selection'))
        if variety==1 or variety ==2 or variety==3:
            basis = variety
        else:
            print "Invalid Selection!"
            exit(0)
        # Define relationship of each
        options = 'Possible Operation Choices:\n[1] Sequential\n[2] Interdependent:'
        print options
        opt = int(input('Enter a Selection: '))
        if opt == 1 or opt == 2:
            op_mode = opt
        else:
            print "Invalid Selection!"
            exit(0)
        # Generate function and evaluate
        return height, width, basis, op_mode

