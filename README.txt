CS 121 - Assignment 1: Text Processing
Note: Numbers within parentheses refer to the line it is on in code.

-----------------------------------------Part A Explanation-----------------------------------------

-----TOKEN CLASS-----
I first made a Token class (6) because I assumed there might be additional functions I would need
that the regular string class lacks. I started out with just the __init__() (9) and token() (22)
functions to initialize a new Token object and a getter to access the _token string stored within it.

-----TOKENIZE()-----
Then I made tokenize() (59), where I opened the given parameter text_file_path (64) and did error
checking (63 & 67-68) for in case if the file cannot be opened. If the file fails to open/cannot be
read, then it simply returns an empty list of tokens (61 & 70). The Tokens yielded by the helper
function _parse_file() are appended to the list token_list (65-66).
-----_PARSE_FILE()-----
I made a separate _parse_file() (78) helper function that takes the opened file and had it read
line by line (82) until the end of the file (81 & 83-84). Since I planned to split each line by
non-alphanumeric characters, I first replaced every non-alphanumeric character with a space (87),
and then split up the remaining characters by whitespace (88). For each parsed word, I made it into
a Token object (90), where I ensured that it had no trailing whitespace and was case-insensitive
(12). I also reject the Token as bad input if a non-English character is found in it (15-17) by
throwing a custom exception BadInput (3-4 & 17). I catch the BadInput exception in a try-except
clause (89 & 92-93) and continue parsing Tokens without including the bad input. I originally
appended directly to the token_list in tokenize() before, but when I started on PartB, I changed
_parse_file() to be a generator instead to make it more reusable by yielding the good Tokens (91).

-----COMPUTEWORDFREQUENCIES()-----
This function takes the completed token_list and counts the times each Token in the list appears by
looping through the list (102). If the Token has yet to be seen (103), then it is added to the
Token dictionary token_dict for the first time and its count is set to one (104). Otherwise, its
count increases by one (105-106). Since the function utilizes a dictionary, to use the Token class
in a dictionary, it needs to have both the __eq__() (40-42) and __hash__(46-48) functions, which I
added to the class. The completed token_dict is then returned (108).

-----PRINTFREQUENCIES()-----
I took the completed token_dict and sorted it first by Token count frequency (high -> low), then
alphabetical order (a -> z) (116). I made a helper function _sort_frequencies to do that. Then I
looped through the dictionary to print out each Token and its count (117-118).
-----_SORT_FREQUENCIES()-----
I made a new dictionary called ordered that will contain all the contents of token_dict but sorted
(126). My plan was to iterate through token_dict, pick out the Token with the greatest frequency and
highest priority in alphabetical order, so I had to keep track of the greatest Token and its count
(128-129). Since alphabetical sorting was involved, I had to add comparison operators __lt__() and
__le__() (28-36). I only had to add those two because I already added __eq__() earlier, and their
negations __gt__(), __ge__(), and __ne__() are automatically provided.
I looped through all items within token_dict (133) until I found the Token currently
within it that had the largest count (134) and saved it to the variables keeping track (135-136).
Once I found it, I added it to ordered and removed it from token_dict (138), then reset the count
(140-141) to repeat iterating through token_dict until every item had been removed and added to
ordered in sorted order (132). I then returned ordered (143).

-----MISC-----
I added __repr__() for testing, so I could see the object's information instead of its memory
address (50-53).


-----------------------------------------Part B Explanation-----------------------------------------
-----MAIN-----
I made a helper function to print out the common Tokens in the two given files. I imported sys (1)
to take the two files given as system arguments (29-30) and put them into _print_common() (31).

-----_PRINT_COMMON()-----
I imported tokenize() and _parse_file() from PartA to avoid code duplication (3), and used
tokenize() on input_file_1 to create a list of the Tokens within it, then turned the list into a set
because I only care about the different Tokens within the first file and not their counts (12). I
then kept a count variable (14) that tallies up each Token in input_file_2 that matches the Token
in the first file (20). I open input_file_2 (16) and send the file to _parse_file() (18), then
check if each yielded Token was within the set of Tokens from the first file (19). If so, I counted
it (20), printed it out (21), and then removed it from the set because it was already accounted for
(22). If input_file_2 failed to open (15 & 23-24), then a count of 0 is printed (25).