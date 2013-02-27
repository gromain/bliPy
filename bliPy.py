#!/usr/bin/env python

import time
import sys
import os
import subprocess
import random

path = '/home/pi/blink1/blink1-tool'  #TO BE REPLACED BY YOUR OWN BLINK1-TOOL ADDRESS

cmd_on = ' --on'
cmd_off = ' --off'
cmd_red = ' --red'
cmd_green = ' --green'
cmd_blue = ' --blue'
cmd_rgb = ' --rgb '
cmd_blink = ' --blink '
cmd_random = ' --random '
cmd_list = ' --list'
cmd_version = ' --version'

opt_fade = ' -m '       # written in milliseconds
opt_timing = ' -t '     # written in milliseconds


def emitCommand(command):
    output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = output.stdout.read()
    return output


class Blink1:
    def __init__(self):
        output = emitCommand(path + cmd_list)
        if (output[:2] == 'no'):
            raise NameError('No blink1 Device Found!')

    def breath(self, interval, rgb=None):
        command = path + opt_fade + str(interval * 1000 / 2) + cmd_off
        emitCommand(command)
        time.sleep(interval / 2)
        if(rgb is not None):
            color = ','.join(str(x) for x in rgb)
            command = (path + opt_fade + str(interval * 1000 / 2) + cmd_rgb
                       + color)
        else:
            command = path + opt_fade + str(interval * 1000 / 2) + cmd_on
        emitCommand(command)

    def breathrand(self, interval):
        command = path + opt_fade + str(interval * 1000 / 2) + cmd_off
        emitCommand(command)
        time.sleep(interval / 2)
        rgb = Blink1.colors[random.choice(Blink1.colors.keys())]
        color = ','.join(str(x) for x in rgb)
        command = path + opt_fade + str(interval * 1000 / 2) + cmd_rgb + color
        emitCommand(command)

    def fade(self, interval, rgb=None):
        if(rgb is not None):
            color = ','.join(str(x) for x in rgb)
            command = (path + opt_fade + str(interval * 1000 / 2) + cmd_rgb
                       + color)
        else:
            command = path + opt_fade + str(interval * 1000 / 2) + cmd_on
        emitCommand(command)

    def fadeseq(self, interval):
        for color in Blink1.colors.keys():
            self.fade(interval, Blink1.colors[color])
            time.sleep(interval)

    def fadetorand(self, interval):
        rgb = Blink1.colors[random.choice(Blink1.colors.keys())]
        color = ','.join(str(x) for x in rgb)
        command = path + opt_fade + str(interval * 1000 / 2) + cmd_rgb + color
        emitCommand(command)

    def rand(self, interval):
        command = path + opt_fade + str(interval * 1000 / 2) + cmd_random
        emitCommand(command)

    def blink(self, interval):
        command = path + opt_fade + str(interval * 1000 / 2) + cmd_blink + '1'
        emitCommand(command)

    colors = {'RED': [255, 0, 0],
              'ORANGE': [255, 125, 0],
              'YELLOW': [255, 255, 0],
              'SPRING_GREEN': [125, 255, 0],
              'GREEN': [0, 255, 0],
              'TURQUOISE': [0, 255, 125],
              'CYAN': [0, 255, 255],
              'OCEAN': [0, 125, 255],
              'BLUE': [0, 0, 255],
              'VIOLET': [125, 0, 255],
              'MAGENTA': [255, 0, 255],
              'RASPBERRY': [255, 0, 125],
              'WHITE': [255, 255, 255],
              'GREY': [125, 125, 125]}
