
#importing datetime module for now()  
from datetime import datetime, timedelta  
  
# using now() to get present_time  
present_time = datetime.now()  
  
#time formatting
'{:%H:%M:%S}'.format(present_time)    
   
print("Present time at greenwich meridian is "
      ,end = "")  
print( present_time )


#importing datetime module for now()  
from datetime import datetime, timedelta  
  
# using now() to get present_time  
present_time = datetime.now()  
  
#time formatting
'{:%H:%M:%S}'.format( present_time )    
   
print("Present time at greenwich meridian is ",
       end = "")  
print( present_time )
  
updated_time = datetime.now() + timedelta(hours=8)
print( updated_time )
from datetime import datetime
from datetime import timedelta
from datetime import date
#today = date.today()
import datetime
#now = datetime.datetime.now()
print ("Notes Tool for the Tickets : ")
#print (now.strftime("%m/%d/%Y %H:%M"))


print('Copy and paste this for the time of the call')
ticket1 = input()

print('Enter the Customer Name:')
ticket2 = input()

print('Enter the reason for the call:')
ticket3 = input()

print('Enter the action that you want to take took:')
ticket4 = input()

print('Who did you give an updated Packing Slip to?:')
ticket5 = input()

print('Enter any Notes:')
ticket6 = input()

#print('Date : ', today, now)
print(ticket1 +' I worked on this ticket. The following is the customer: '+ ticket2 +'. The customer called about the following - ' + ticket3 + ' Remedy: ' + ticket4 + ' Then I gave a copy of Packing Slip to ' + ticket5 + '. NOTES: ' + ticket6)
