// You are given a string s of lowercase English letters.

// Call the shift() of a letter, the next letter in the alphabet, 
//(wrapping around so that 'z' becomes 'a').

// For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
// Now for each i, we want to shift the first i + 1 letters of s, i+1 times.

// Return the final string after all such shifts to s are applied.

// s = "abc"  result = "ddd"
// s = "aaa"  result = "dcb"


// s = "abc"  result = "ddd"
/*
right increase char shift by one time

abc 
321

shift = 1
sum = 0 
for right to left 
     char -> shift(shift+sum)

return string_changed 

time complexity O(n) n is size of array 
space complexity o(1)

min length of string 0 
max len 10^5

*/


#include<string>

using namespace std;


string shiftString(string str)
{
    if(str.size()==0)
        return "";
    
    int shift = 1;
    int sum = 0;
    int maxChar = 26;

    for(int i = str.size()-1;i>=0;i--)
    {
        sum = (sum+shift)%maxChar;      // safeguard, since max value of sum = 25
        str[i] = (str[i]-'a'+sum)%maxChar + 'a';
    }

    return str;
    
}










