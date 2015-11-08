#!/usr/bin/env python
# coding=UTF-8


# 阿拉伯數字 -> 中文數字
chinese_num_char = [u"零", u"一", u"二", u"三", u"四", u"五", u"六", u"七", u"八", u"九"]	#中文數字
chinese_unit_section = [u"", u"萬", u"億", u"萬億"]	# 節權位
chinese_unit_char = [u"", u"十", u"百", u"千"]	# 權位

def number_to_chinese(number):
	'''
	Input:
		number: 阿拉伯數字(正整數)
	Output:
		chinese_str: 中文數字
	'''
	
	chinese_str = ""	# 輸出的中文數字
	
	unit_position = 0
	str_insert = ""		# 每小節的中文數字
	need_zero = False
	
	while(number > 0):
		# 每次處理一小節
		section = number % 10000
		
		# 如果前一個小節判斷需要補零(千位是零，但整個小節不是零)，在本小節一開始就先補
		if (need_zero):
			chinese_str = chinese_num_char[0] + chinese_str
		
		if (section != 0):
			# 將本小節的阿拉伯數字轉換成中文數字
			str_insert = section_to_chinese(section)
			# 加上節權位
			str_insert = str_insert + chinese_unit_section[unit_position]
		
		# 合併字串
		chinese_str = str_insert + chinese_str
		
		# 判斷下一小節需不需要補零
		if (section < 1000) and (section > 0):
			need_zero = True
		
		number = number / 10000
		unit_position += 1
	
	return chinese_str

	
def section_to_chinese(section):
	'''
	Input:
		section: 阿拉伯數字(正整數)
	Output:
		chinese_str: 中文數字
	'''
	chinese_str = ""
	str_insert = ""
	unit_position = 0
	zero = True # 尾端的0不需要補零
	
	while(section > 0):
		v = section % 10
		
		if (v == 0):
			# 確保連續的0只會轉換成一個零
			if (not zero):
				zero = True	
				chinese_str = chinese_num_char[v] + chinese_str
		
		else:
			zero = False
			str_insert = chinese_num_char[v]	# 此位對應的中文數字
			str_insert += chinese_unit_char[unit_position]	# 此位對應的中文權位
			chinese_str = str_insert + chinese_str
		
		unit_position += 1
		section = section / 10
	
	return chinese_str

# 中文數字 -> 阿拉伯數字
# 中文權位與10的倍數的關係表
class chn_name_value:
	def __init__(self, name, value, section_unit):
		self.name = name	# 中文權位名稱
		self.value = value	# 10的倍數值
		self.section_unit = section_unit	# 是否是節權位
	
chn_value_pair = []
chn_value_pair.append(chn_name_value(u"十", 10, False))
chn_value_pair.append(chn_name_value(u"百", 100, False))
chn_value_pair.append(chn_name_value(u"千", 1000, False))
chn_value_pair.append(chn_name_value(u"萬", 10000, True))
chn_value_pair.append(chn_name_value(u"億", 100000000, True))

def chinese_to_number(chinese_str):
	'''
	Input: 
		chinese_str	中文數字
	Output:
		rtn	阿拉伯數字
	'''
	rtn = 0
	section = 0
	number = 0
	section_unit = False
	position = 0
	
	# 轉換成big5格式
	if type(chinese_str) is str:
		chinese_str = chinese_str.decode('big5')
	
	while(position < len(chinese_str)):
		num = chinese_to_value(chinese_str[position])
		if (num >= 0):	# 數字
			number = num
			position +=1
			if (position >= len(chinese_str)):
				section += number
				rtn += section
				break
		else:	# 單位
			(unit, section_unit) = chinese_to_unit(chinese_str[position])
			if section_unit:
				section = (section + number) * unit
				rtn += section
				section = 0
			else:
				section += number * unit
			
			number = 0
			position += 1
			if (position >= len(chinese_str)):
				rtn += section
				break
	
	return rtn

def chinese_to_value(chinese_str):
	for i in range(len(chinese_num_char)):
		if chinese_num_char[i] == chinese_str:
			return i
	return -1

def chinese_to_unit(chinese_str):
	for pair in chn_value_pair:
		if pair.name == chinese_str:
			return (pair.value, pair.section_unit)
			
if __name__ == "__main__":
	s = number_to_chinese(200001010200)
	print(s)#.decode('utf-8')#.encode('big5')
	n = chinese_to_number(u'二千億零一百零一萬零二百')
	print(n)





	
	
