'''
Write a python program to perform the following operations on the given string using the various regular expression functions.
flight_details="Good Evening, Welcome to British Airways. Your flight number is ba8004. Flight departure time is 16:45"

1. Find whether the flight service name, British Airways is present in the given string and if so, display it.
2. Find whether the flight details ends with the departure time, 16:45 and if so, display it.
3. Find whether the flight details starts with "Good" and if so, display it.
4. Find a word which starts with 'F' and having 6 characters in it, if so display it.
5. Search for a word which starts with "ba" followed by exactly 4 digits. If found, replace the two alphabets with the corresponding uppercase
alphabets.
For questions 1 to 4, if the searched pattern is not present, display "No Output"
'''


#PF-Tryout
import re

flight_details="Good Evening, Welcome to British Airways. Your flight number is ba8004. Flight departure time is 16:45"

#This function returns the values in the search result
def printout(search_result):
    if(search_result!=None):
        return search_result.group()
    else:
        return "No Output"

search_result = re.search(r"British Airways",flight_details)
#Write your regular expression here for question 1
#This will invoke the printout() and displays the search result values
print(printout(search_result))

search_result = re.search(r"16:45$",flight_details)
#Write your regular expression here for question 2
print(printout(search_result))

search_result = re.search(r"^Good",flight_details)
#Write your regular expression here for question 3
print(printout(search_result))

search_result = re.search(r"F.....",flight_details)
#Write your regular expression here for question 4
print(printout(search_result))

print(re.sub(r"ba(\d{4})",r"BA\1",flight_details))
