#include <vector>
#include <string>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 1. 准备哈希表
        // Key 是字符串的特征（比如字母频率拼接成的字符串）
        // Value 是一个向量（类似 Python 的列表），存放同组的字符串
        unordered_map<string, vector<string>> groups;

        // 2. 遍历每个字符串
        for (const string& s : strs) {
            // 准备一个长度为 26 的数组，初始化为 0
            int count[26] = {0}; 
            
            // 统计字母频率
            for (char c : s) {
                count[c - 'a']++;
            }

            // 3. 构建独一无二的 Key
            // C++ 中没有像 Python 那么方便的 join，我们手动拼一下
            // 为了防歧义，用 '#' 隔开（比如 "1#0#1#..."）
            string key = "";
            for (int i = 0; i < 26; i++) {
                key += to_string(count[i]) + "#";
            }

            // 4. 直接存入哈希表
            // 如果 key 不存在，C++ 的 unordered_map 会自动创建并赋值一个空 vector
            // 这跟 Python 的 defaultdict(list) 行为一模一样
            groups[key].push_back(s);
        }

        // 5. 把字典里的值全部拿出来返回
        vector<vector<string>> result;
        for (auto& pair : groups) {
            result.push_back(pair.second); // pair.second 就是那个 vector<string>
        }

        return result;
    }
};