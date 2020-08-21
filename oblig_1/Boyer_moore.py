import PyPDF2
import string

# Bruker kanskje litt lang tid på å søke? Én årsak er at alfabetet inkluderer diverse tegn utover det norske...

file = open('et_dukkehjem.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(file)
pages = pdf_reader.numPages


# indekserer string ved bruk av dictionary. Legg til karakterer som ikke finnes i dict dersom programmet feiler,
# i 'alphabet_dict'. Lesson learned; Ikke bruk fortellinger med gammelt språk.
def index_string(p: str):
	alphabet_dict = dict.fromkeys(string.printable + "œæøå\néè«™", -1)
	
	# Kan legge inn en sjekk for duplikater, men unødvendig når p er/skal være 5 karakterer lang.
	for i in p:
		d = {i: p.rfind(i)}
		alphabet_dict.update(d)
	return alphabet_dict


def BMAlgorithm(t, p):
	dict_temp = index_string(pattern)
	m = len(p)
	n = len(t)
	i = m - 1
	j = m - 1
	counter = 0
	
	while i < n:
		counter += 1
		if t[i] == p[j]:
			if j == 0:
				print('Snitt pr. karakter: %s ' % (counter / i))
				return i
			else:
				i -= 1
				j -= 1
		else:
			foo = dict_temp.get(t[i])
			# Kommenter ut denne dersom programmet feiler for å finne karakter i debug-mode.
			# print(t[i])
			i = i + m - min(j, 1 + foo)
			j = m - 1
	print('Snitt pr. karakter: %s ' % (counter / i))
	return -1


def init():
	pdf_string = ""
	for ii in range(pages):
		page = pdf_reader.getPage(ii)
		pdf_string += page.extractText().lower()
	return pdf_string


if __name__ == "__main__":
	def show(t, p):
		ps = BMAlgorithm(t, p)
		print('Match: i = %s' % ps)
		print('Pattern: %s' % p)
	
	
	pattern = "skyde"  # Sett inn mønster her...
	text = init()
	show(text, pattern)
