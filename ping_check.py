import commands
ip='172.31.31.54'
cmd="ping -c 4 " + ip + "| grep transmitted | awk ' {if ($1==$4)  print 1; else print 0 }'"
#status,output = commands.getstatusoutput("ping -c 4 ip | grep transmitted | awk ' $1==$4 ? i=1: i=0 {print i}'")
status,output = commands.getstatusoutput(cmd)
print ip + ":" +output
