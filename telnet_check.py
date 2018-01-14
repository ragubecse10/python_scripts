import commands
ip='172.31.31.54'
cmd="nmap -A " + ip + " -p 22 | grep open | grep /tcp | wc -l"
status,output = commands.getstatusoutput(cmd)
print ip + ":" +output
