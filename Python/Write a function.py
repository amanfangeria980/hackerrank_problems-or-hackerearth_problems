def is_leap(year):
    leap = False
    if year%100!=0 and year%4==0:
        leap = True
        return leap
    elif year%100==0 and year%400==0:
        leap = True;
        return leap
    else:
        return leap
    
    # Write your logic here
    
  
