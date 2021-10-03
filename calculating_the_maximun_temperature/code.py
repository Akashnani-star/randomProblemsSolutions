def calculateMax(data,n=0):
	# removing empty lines in the data of file
	while("" in data):
		data.remove("")
	
	# formatting the data with year and temp into final_data list
	final_data = []
	for i in data:
		if(i[92] != "1"):
			continue
		else:
			temp = ""
			string_temp = i[87:92]
			for j in range(len(string_temp)):
				if(j == len(string_temp) - 1):
					temp += "."
				temp+=string_temp[j]
			final_data.append([i[15:19],float(temp)])
	
	# calculating maximum temperature and line number of that temperature using the final_data list
	max = -30000.0
	count = 0
	line = 0
	for i in final_data:
		count+=1
		if(max < i[1]):
			max = i[1]
			line = count
	return (max,line)

# reading the files
file1 = open("datasets/1901.txt")
file2 = open("datasets/1902.txt")


# calculating the max temp for file 1
# getting the data of file as list with lines as elements of list
data = file1.read().split("\n")
# calculating the max temperature
ans = calculateMax(data)
# printing it to the screen
print(ans[0],"degress,","In line Number : ",ans[1])

# calculating the max temp for file 2
# getting the data of file as list with lines as elements of list
data = file2.read().split("\n")
# calculating the max temperature
ans = calculateMax(data)
# printing it to the screen
print(ans[0],"degress,","In line Number : ",ans[1])
