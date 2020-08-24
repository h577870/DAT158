from time import time

# Dynamisk algoritme
def lcs_dyn(x, y):
	m = len(x)
	n = len(y)
	# generator
	l = [[0] * (n + 1) for i in range(m + 1)]
	
	# Testing av tidsbruk
	timer_1 = time()
	
	for i in range(m + 1):
		for j in range(n + 1):
			# Første rad / kolonne
			if i == 0 or j == 0:
				l[i][j] = 0
			# Hvis tegn i f.eks. x[1] == y[1]
			elif x[i - 1] == y[j - 1]:
				# plass [i][j] får verdi 1 + l[i-1][j-1]
				l[i][j] = l[i - 1][j - 1] + 1
			else:
				# Ulike tegn, [i][j] får verdi fra maks(over, venstre)
				l[i][j] = max(l[i - 1][j], l[i][j - 1])
	timer_2 = time()
	print(f"Tidsbruk: %s" % (timer_2 - timer_1).__format__('.6f'))
	return l[m][n]


# Rekursiv algoritme
def lcs_rec(x, y, m, n):
	if n == 0 or m == 0:
		return 0
	elif x[m - 1] == y[n - 1]:
		return 1 + lcs_rec(x, y, m - 1, n - 1)
	else:
		return max(lcs_rec(x, y, m - 1, n), lcs_rec(x, y, m, n - 1))
