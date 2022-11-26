# hrs_passed = int(input('hrs passed '))
# mins_passed = int(input('minutes passed '))

hrs_degree = 30
min_degree = 6
hrs_passed = 6
mins_passed = 15

if (mins_passed == 0):
    degree_for_mins = 0
else:
    degree_for_mins = (mins_passed/60) * 360

if (hrs_passed == 12 or hrs_passed == 0):
    degree_for_hrs = 0
else:
    degree_for_hrs = hrs_passed * hrs_degree


hrs_hand_procceded = hrs_degree * (mins_passed/60)

print((degree_for_hrs+hrs_hand_procceded))
res = degree_for_mins-(degree_for_hrs+hrs_hand_procceded)

print(res)
if res < 0 :
    print(f'mins to hrs is {360+res}')
else:
    print(f'hrs to mins is {res}')
        
# Hrs 
