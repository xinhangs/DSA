#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (char c : s)
        {
            switch(c)
            {
                case '{':
                case '[':
                case '(':
                    stk.push(c);
                    break;
                case '}':
                    if (stk.empty())
                        return false;
                    else
                        if (stk.top() == '{')
                            stk.pop();
                        else
                            return false;
                    break;
                case ']':
                    if (stk.empty())
                        return false;
                    else
                        if (stk.top() == '[')
                            stk.pop();
                        else
                            return false;
                    break;
                case ')':
                    if (stk.empty())
                        return false;
                    else
                        if (stk.top() == '(')
                            stk.pop();
                        else
                            return false;
                    break;
                default:
                    break;
            }
        }
        return stk.empty();
    }
};