
inputFile=open('abc.txt','r')
outputFile=open('Output.txt','w')
data=inputFile.read()
outputFile.write(data)
inputFile.close()
outputFile.close()