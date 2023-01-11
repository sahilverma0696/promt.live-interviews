#include<string>


using namespace std;

// You are given a string s of lowercase English letters.

// Call the shift() of a letter, the next letter in the alphabet, 
// (wrapping around so that 'z' becomes 'a').

// For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
// Now for each i, we want to shift the first i + 1 letters of s, i+1 times.

// Return the final string after all such shifts to s are applied.

// s = "abc"  result = "ddd"
// s = "aaa"  result = "dcb"


/*
"" -> return ""

a -> b
ab -> cc

starting from the right 
1,2,3,4,5,6

abcdef
654321

sum  = 0
str[size-1] -> shift(1)

O(n)

*/


string shiftChar(string s)
{
    int shift = 1;
    int maxChar = 26;
    if(s.size()==0)
        return "";
    int sum  = 0;
    for(int i = s.size()-1;i>=0;i--)
    {
        sum +=shift;
        s[i] = (s[i]-'a'+sum)%maxChar+'a';
    }
    return s;
}



