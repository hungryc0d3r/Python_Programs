# Python_Programs
python programs practicing

string methods
---------------
str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

A string of text can be aligned left, right and center.
------------------------------------

.ljust(width)
This method returns a left aligned string of length width.
    
    width = 20
    print 'HackerRank'.ljust(width,'-') 
    HackerRank----------  
      
.center(width)
This method returns a centered string of length width.

      width = 20
      print 'HackerRank'.center(width,'-')
      -----HackerRank-----
      
.rjust(width)
This method returns a right aligned string of length width.

      width = 20
      print 'HackerRank'.rjust(width,'-')
      ----------HackerRank
