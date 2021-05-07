def table():
	t=input("What tables would you like to display: ")
	t=int(t)
	for i in range(11):
			print(t,"x",i,"=",t*i)
	s=input("D0 you want to try tables again? yes/no ")
	s=str(s)
	if (s == "yes"):
		table()
	if (s == "no"):
		exit()
table()