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

from LIS3DHH_constants import *

# name:        LIS3DHH
# description: MEMS digital output motion sensor ultra low-power high performance 3-axes 'nano' accelerometer
# manuf:       ST Microelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/lis3dhh.pdf
# date:        2018-01-26


# Derive from this class and implement read and write
class LIS3DHH_Base:
	"""MEMS digital output motion sensor ultra low-power high performance 3-axes 'nano' accelerometer"""
	# Register WHO_AM_I
	# 7.1
	#       Device identification register. 
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register CTRL_REG1
	# 7.2
	#       Control register 1. 
	
	
	def setCTRL_REG1(self, val):
		"""Set register CTRL_REG1"""
		self.write(REG.CTRL_REG1, val, 8)
	
	def getCTRL_REG1(self):
		"""Get register CTRL_REG1"""
		return self.read(REG.CTRL_REG1, 8)
	
	# Bits NORM_MOD_EN
	# Normal mode enable. 
	# Bits IF_ADD_INC
	# Register address automatically incremented during a multiple byte access with SPI serial interface. 
	# Bits reserved_0
	# These bits must be set to ‘0’ for the correct operation of the device. 
	# Bits BOOT
	# Reboot memory content. 
	#           Boot request is executed as soon as the internal oscillator is turned on. It is possible to set the bit 
	#           while in power-down mode, in this case it will be served at the next normal mode. 
	
	# Bits SW_RESET
	# Software reset. 
	#           With SW_RESET the values in the writable CTRL registers are changed to the default values. 
	#           This bit is cleared by hardware at the end of the operation.  
	
	# Bits DRDY_PULSE
	# Data ready on INT1 pin. 
	# Bits BDU
	# Block Data Update. 
	# Register INT1_CTRL
	# 7.3
	#       INT1 pin control register. 
	
	
	def setINT1_CTRL(self, val):
		"""Set register INT1_CTRL"""
		self.write(REG.INT1_CTRL, val, 8)
	
	def getINT1_CTRL(self):
		"""Get register INT1_CTRL"""
		return self.read(REG.INT1_CTRL, 8)
	
	# Bits INT1_DRDY
	# Accelerometer data ready on INT1 pin. 
	# Bits INT1_BOOT
	# Boot status available on INT1 pin. 
	# Bits INT1_OVR
	# Overrun flag on INT1 pin. 
	# Bits INT1_FSS5
	# FSS5 full FIFO flag on INT1 pin. 
	# Bits INT1_FTH
	# FIFO threshold flag on INT1 pin. 
	# Bits INT1_EXT
	# INT1 pin configuration.
	#             It configures the INT1 pad as output for FIFO flags or as external asynchronous input trigger to FIFO.
	#             INT2 pad is always available as output for FIFO flags. 
	
	# Bits reserved_0
	# These bits must be set to ‘0’ for the correct operation of the device. 
	# Register INT2_CTRL
	# 7.4
	#       INT2 pin control register. 
	
	
	def setINT2_CTRL(self, val):
		"""Set register INT2_CTRL"""
		self.write(REG.INT2_CTRL, val, 8)
	
	def getINT2_CTRL(self):
		"""Get register INT2_CTRL"""
		return self.read(REG.INT2_CTRL, 8)
	
	# Bits INT2_DRDY
	# Accelerometer data ready on INT2 pin. 
	# Bits INT2_BOOT
	# Boot status available on INT2 pin. 
	# Bits INT2_OVR
	# Overrun flag on INT2 pin. 
	# Bits INT2_FSS5
	# FSS5 full FIFO flag on INT2 pin. 
	# Bits INT2_FTH
	# FIFO threshold flag on INT2 pin. 
	# Bits reserved_0
	# These bits must be set to ‘0’ for the correct operation of the device. 
	# Register CTRL_REG4
	# 7.5
	#       Control register 4. 
	
	
	def setCTRL_REG4(self, val):
		"""Set register CTRL_REG4"""
		self.write(REG.CTRL_REG4, val, 8)
	
	def getCTRL_REG4(self):
		"""Get register CTRL_REG4"""
		return self.read(REG.CTRL_REG4, 8)
	
	# Bits DSP_LP_TYPE
	# Digital filtering selection. 
	# Bits DSP_BW_SEL
	# User-selectable bandwidth. 
	# Bits ST
	# Self-test enable. 
	# Bits PP_OD_INT2
	# Push-pull/open drain selection on INT2 pin. 
	# Bits PP_OD_INT1
	# Push-pull/open drain selection on INT1 pin. 
	# Bits FIFO_EN
	# FIFO memory enable. 
	# Bits reserved_0
	# This bit must be set to ‘1’ for correct operation of the device. 
	# Register CTRL_REG5
	# 7.6
	#       Control register 5. 
	
	
	def setCTRL_REG5(self, val):
		"""Set register CTRL_REG5"""
		self.write(REG.CTRL_REG5, val, 8)
	
	def getCTRL_REG5(self):
		"""Get register CTRL_REG5"""
		return self.read(REG.CTRL_REG5, 8)
	
	# Bits reserved_0
	# These bits must be set to ‘0’ for correct operation of the device. 
	# Bits FIFO_SPI_HS_ON
	# Enables the SPI high speed configuration for the FIFO block that is used to guarantee a 
	#           minimum duration of the window in which writing operation of RAM output is blocked. 
	#           This bit is recommended for SPI clock frequencies higher than 6 MHz. 
	
	# Register OUT_TEMP
	# 7.7
	#       Temperature data output register. L and H registers together express a 16-bit word in two’s complement 
	#       left-justified. 
	
	
	def setOUT_TEMP(self, val):
		"""Set register OUT_TEMP"""
		self.write(REG.OUT_TEMP, val, 16)
	
	def getOUT_TEMP(self):
		"""Get register OUT_TEMP"""
		return self.read(REG.OUT_TEMP, 16)
	
	# Bits unused_0
	# Bits Temp
	# Temperature sensor output data.
	#           The value is expressed as two’s complement sign.
	#           0 LSB represents T=25 °C ambient. 
	
	# Register STATUS
	# 7.8
	#       Status register (r) 
	
	
	def setSTATUS(self, val):
		"""Set register STATUS"""
		self.write(REG.STATUS, val, 8)
	
	def getSTATUS(self):
		"""Get register STATUS"""
		return self.read(REG.STATUS, 8)
	
	# Bits ZYXOR
	# Logic OR of the single X-, Y- and Z-axis data overrun. 
	# Bits ZOR
	# Z-axis data overrun. 
	# Bits YOR
	# Y-axis data overrun. 
	# Bits XOR
	# X-axis data overrun. 
	# Bits ZYXDA
	# Logic AND of the single X-, Y- and Z-axis new data available. 
	# Bits ZDA
	# Z-axis new data available. 
	# Bits YDA
	# Y-axis new data available. 
	# Bits XDA
	# X-axis new data available. 
	# Register OUT_X
	# 7.9
	#       Linear acceleration sensor X-axis output register. The value is expressed as a 16-bit 
	#       word in two’s complement. 
	
	
	def setOUT_X(self, val):
		"""Set register OUT_X"""
		self.write(REG.OUT_X, val, 16)
	
	def getOUT_X(self):
		"""Get register OUT_X"""
		return self.read(REG.OUT_X, 16)
	
	# Bits OUT_X
	# Register OUT_Y
	# 7.10
	#       Linear acceleration sensor Y-axis output register. The value is expressed as a 16-bit 
	#       word in two’s complement. 
	
	
	def setOUT_Y(self, val):
		"""Set register OUT_Y"""
		self.write(REG.OUT_Y, val, 16)
	
	def getOUT_Y(self):
		"""Get register OUT_Y"""
		return self.read(REG.OUT_Y, 16)
	
	# Bits OUT_Y
	# Register OUT_Z
	# 7.11
	#       Linear acceleration sensor Z-axis output register. The value is expressed as a 16-bit 
	#       word in two’s complement. 
	
	
	def setOUT_Z(self, val):
		"""Set register OUT_Z"""
		self.write(REG.OUT_Z, val, 16)
	
	def getOUT_Z(self):
		"""Get register OUT_Z"""
		return self.read(REG.OUT_Z, 16)
	
	# Bits OUT_Z
	# Register FIFO_CTRL
	# 7.12
	#       FIFO control register. 
	
	
	def setFIFO_CTRL(self, val):
		"""Set register FIFO_CTRL"""
		self.write(REG.FIFO_CTRL, val, 8)
	
	def getFIFO_CTRL(self):
		"""Get register FIFO_CTRL"""
		return self.read(REG.FIFO_CTRL, 8)
	
	# Bits FMODE
	# FIFO mode selection bits. 
	# Bits FTH
	# FIFO threshold level setting. 
	# Register FIFO_SRC
	# 7.13
	#       FIFO status register. 
	
	
	def setFIFO_SRC(self, val):
		"""Set register FIFO_SRC"""
		self.write(REG.FIFO_SRC, val, 8)
	
	def getFIFO_SRC(self):
		"""Get register FIFO_SRC"""
		return self.read(REG.FIFO_SRC, 8)
	
	# Bits FTH
	# FIFO threshold status. 
	# Bits OVRN
	# FIFO overrun status. 
	# Bits FSS
	# Number of unread samples stored in FIFO.
	#           When the number of unread samples in FIFO is equal to or greater than the threshold level set in register FIFO_CTRL (2Eh), the FTH value is ‘1’. 
	#           The FSS is the FIFO stored data level of the unread samples. When it is equal to FTH, all data available in FIFO are read without additional read operations.
	#           The INT output is high when the number of samples to read is equal to or greater than FTH. 
	
