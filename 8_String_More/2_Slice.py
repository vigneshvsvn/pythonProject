"""
- To Take part or slice of String. We need to use Slice Operator.
- Syntax: s[begin:end:step]
	Eg: name[begin:end] --> slice begin to end -1 index data.
	- step means how much increment need to do. Default will be 1
"""
name="Vignesh"
print(name[0:])   ## End is optional. So end will consider end of String by default
print(name[:5])  ## If Begin is optional, So Begin will consider 0 index until 5-1 index.
print(name[1:5]) ## index to 5-1 index
print(name[:])   ## begin to end all char will print. As Begin will consider 0 index and end index will consider len(name)
print(name[1:5:2])

"""
Rules:
step: +ve --> forward direction --> Left to Right --> Begin to end-1
	  -ve --> Backward direction --> Right to left --> begin to end+1
	 step value can't be zero.

Default values :
Forward Direction: Begin --> 0 index ; end  --> len(str)
				-  Eg: "Vignesh" 0--> v ; 1--> i ; 2--> g ; 3 --> n ;4  --> e ;5 --> s; 6 --> h
Backward Direction: begin --> -1 index; end --> -(len(str) + 1)
				- Eg: "Vignesh"    -1 --> h; -2-->s ; -3 --> e ; -4 --> n ; -5 --> g ; -6 --> i ; -7 --> v
"""
s='abcdefghij'
print(s[1:6:2])
print(s[::1])
print(s[::-1])    ## Note reverse the string
print(s[3:7:-1])
print(s[7:4:-1])     ## Back Ward Direction : So start:7  end = 4+1
print(s[0:1000:1])   ## All available index will print
print(s[-4:1:-1]) ## start: -4 end 1+1(as backward because step is -ve)
print(s[-4:1:-2])
print(s[5:0:1])    ## Empty end value , in forward direction end value is 0 then empty
#print(s[3:0:0])      ## error as step is Zero
print(s[0:-10:-1])
print(s[0:-11:-1])
print(s[0:0:1])
print(s[0:-9:-2])
print(s[-5:-9:-2])
print(s[10:-1:-1]) ## empty as end is -1 for backward direction
print(s[1000:2:-1])  #  