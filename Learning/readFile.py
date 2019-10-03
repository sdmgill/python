#with open('C:\RFCDeploy\Rolling12ImplementationRollback.txt', 'r') as open_file:
 #   all_text = open_file.read()


with open('C:\RFCDeploy\Rolling12ImplementationRollback.txt', 'r') as open_file:
	line = open_file.readline()
	while line:
		print(line)
		line = open_file.readline()
