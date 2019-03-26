
# 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 計數
def count(lines):
	allen_words_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_words_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			for m in s[2:]:
				allen_words_count += len(m)
		if name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			for m in s[2:]:
				viki_words_count += len(m)
	print('Allen說了： ', allen_words_count, '個字')
	print('Allen傳了： ', allen_sticker_count, '個貼圖')
	print('Allen傳了： ', allen_image_count, '張照片')
	print('Viki說了： ', viki_words_count, '個字')
	print('Viki傳了： ', viki_sticker_count, '個貼圖')
	print('Viki傳了： ', viki_image_count, '張照片')


def main():
	lines = read_file('[LINE]Viki.txt')
	lines = count(lines)


main()