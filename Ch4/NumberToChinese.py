#!/usr/bin/env python
# coding=UTF-8

chinese_num_char = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]	#中文數字
chinese_unit_section = ["", "萬", "億", "萬億"]	# 節權位
chinese_unit_char = ["", "十", "百", "千"]	# 權位

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
		section = number % 10000
		# 如果前一個小節判斷需要補零(千位是零，但整個小節不是零)，在本小節一開始就先補
		if (need_zero):
			chinese_str = chinese_num_char[0] + chinese_str
		
		str_insert = section_to_chinese(section)
		
		# 是否加上節權位
		if (section != 0):
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
	zero = True
	
	while(section > 0):
		v = section % 10
		
		if (v == 0):
			if (not zero):
				zero = False
				chinese_str = chinese_num_char[v] + chinese_str
		
		else:
			zero = False
			str_insert = chinese_num_char[v]	# 此位對應的中文數字
			str_insert += chinese_unit_char[unit_position]	# 此位對應的中文權位
			chinese_str = str_insert + chinese_str
		
		unit_position += 1
		section = section / 10
	
	return chinese_str


	
if __name__ == "__main__":
	s = number_to_chinese(200001010200)
	print(s).decode('utf-8')#.encode('big5')






	
	
