l, u, p, d = 0, 0, 0, 0
s = input("entre any password  ")
if (len(s) >= 6) or (len(s)<15):
	for i in s:

		# counting lowercase alphabets
		if (i.islower()):
			l = l + 1
            		

		# counting uppercase alphabets
		if (i.isupper()):
			u = u + 1		

		# counting digits
		if (i.isdigit()):
			d = d + 1	

		# counting the mentioned special characters
		if(i=='@'or i=='$' or i=='_' or i=='#' or i =='=' or i =='<'):
			p = p + 1	
if ((l>=1 and l <=10) and (u>=1 and u<=5) and (p>=1 and p<=5) and (d>=1 and d<=5) and l+p+u+d==len(s)):
	print("Valid Password")
else:
	print("Invalid Password !! Password should be at least one lower , one upper , one numberic & one special character ")
    