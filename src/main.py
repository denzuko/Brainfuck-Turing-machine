#!/usr/bin/env python
# -*- coding: utf-8 -*-

import BrainfuckMachine 

def main():

  machine = BrainfuckMachine.BrainfuckMachine(50)
  with open('helloworld.bf', 'r') as f:
    machine.setCode(f.read())

  machine.run()
  print machine.getOutput()

if __name__ is "__main__": main()
