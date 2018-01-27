#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LIS3DHH: MEMS digital output motion sensor ultra low-power high performance 3-axes 'nano' accelerometer"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["ST Microelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

class REG:
	WHO_AM_I = 15
	CTRL_REG1 = 32
	INT1_CTRL = 33
	INT2_CTRL = 34
	CTRL_REG4 = 35
	CTRL_REG5 = 36
	OUT_TEMP = 37
	STATUS = 39
	OUT_X = 40
	OUT_Y = 42
	OUT_Z = 44
	FIFO_CTRL = 46
	FIFO_SRC = 47
