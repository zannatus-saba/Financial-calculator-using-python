# Build a financial calculator

# NPV of the following cashflows with a
# discount rate of 10%

cf = [2000,900,600,300]
r = .10

# Wrong way, since its hard-coded
#   (But still useful to build intuition)
# npv = 2000 / (1+r)**1  \
# 	+ 900 / (1+r)**2  \
# 	+ 600 / (1+r)**3  \
# 	+ 300 / (1+r)**4

# Annual terms
def npv(values, r):
	# Initialze pv to 0
	p0 = 0
	# Loop through all elements in the values input
	for i in range(len(values)):
		p0 += (values[i] / (1+r)**(i+1))
	return(p0)


# Prove that constant growth is a geometric series
D1 = 2
r = .1
g=.05

ver1 = D1/(r-g)
import pandas as pd

# Version 2a
infinite_divs = []
for i in range(5000):
	D_n = D1*(1+g)**i
	infinite_divs.append(D_n)

# Version 2b
infinite_divs = [2] + (pd.Series([1.05]*1000).cumprod()*2).to_list()

npv(infinite_divs,r)



# Non-constant growth, which transitions to constant growth in n years
def npv(values, r, g):
	# Initialze pv to 0
	p0 = 0
	# Loop through all elements in the values input
	for i in range(len(values)):
		p0 += (values[i] / (1+r)**(i+1))
	p0 = p0 + (values[i]*(1+g))/(r-g) / (1+r) ** (i+1)
	return(p0)
