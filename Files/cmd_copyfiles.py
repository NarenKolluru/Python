import sys
name=sys.argv[1]
outputs=open(sys.argv[2],'w')
inputs=open(name,'r')
data=inputs.read()
while data:
    outputs.write(data)
    data=inputs.read()
inputs.close()
outputs.close()
print("File copied successfully")
