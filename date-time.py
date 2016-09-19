# from datetime import timedelta, date ,datetime
#
# def daterange(start_date, end_date):
# 	 for n in range(int ((end_date - start_date).days)):
# 		 yield start_date + timedelta(n)

# print(y1)
# start_date = date(y1, m1, d1)
# end_date = date(y2, m2, d2+1)
# for single_date in daterange(start_date, end_date):
#	 # print(single_date.strftime("%Y-%m-%d"))
#	 y,m,d=map(int ,single_date.strftime("%Y-%m-%d").split('-'))
#	 if d+1==m and m+1==(y%100):
#		 count+=1
# print(count)

n=int(input())
for i in range(n):
	count=0
	data=input()
	date1,date2=map(str , data.split(' '))
	d1, m1, y1 = map(int, date1.split(':'))
	d2, m2, y2 = map(int, date2.split(':'))
	for i in range(y1+1,y2):
		if i%100>=3 and i%100<=13:
			count+=1

	if y1%100>=3 and y1%100<=13 :
		if (y1%100)-1>m1 and y1<y2:
			count+=1
		elif (y1%100)-1>m1 and y1==y2 and (y1%100)-1<m2 :
			count+=1
		elif (y1%100)-1>m1 and y1==y2 and (y1%100)-1==m2 and (m2-1)<=d2 :
			count+=1
		elif (y1%100)-1==m1 and d1+1<=m1 and y1<y2 :
			count+=1
		elif (y1%100)-1==m1 and d1+1<=m1 and y1==y2 and (y1%100)-1<m2 :
			count+=1
		elif (y1%100)-1==m1 and d1+1<=m1 and y1==y2 and (y1%100)-1==m2 and m2-1<=d2:
			count+=1
	# if y1%100>=3 and y1%100<=13:
	# 	count+=1
	if y2%100>=3 and y2%100<=13 and y1<y2:
		if (y2%100)-1<m2:
			count+=1
		elif (y2%100)-1==m2 and d2+1>=m2 :
			count+=1
	print(count)
