// You are given a string s of lowercase English letters and an integer array
// shifts of the same length.

// Call the shift() of a letter, the next letter in the alphabet,
// (wrapping around so that 'z' becomes 'a').

// For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
// Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

// Return the final string after all such shifts to s are applied.


// s = "abc", shifts = [3,5,9] result= "rpl" -> 3+5+9, 5+9, 9
// s = "aaa", shifts = [1,2,3] result= "gfd"
#include<string>
#include<vector>
using namespace std;

string shiftChar(string &s,vector<int> &shifts)
{
    int maxChar = 26;
    if(s.size()==0)
        return "";
    int sum  = 0;
    for(int i = s.size()-1;i>=0;i--)
    {
        sum  = (sum+shifts[i])%26;            // 10 -> sum = 10, 17 10+17 -> 27%26 -> 1
        s[i] = (s[i]-'a'+sum)%maxChar+'a';
    }
    return s;
}