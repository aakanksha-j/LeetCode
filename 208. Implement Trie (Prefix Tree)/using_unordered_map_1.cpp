#include <unordered_map>
#include <string>

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;
    bool is_word_end;
    
    TrieNode() {
        is_word_end = false;
    }
};

class Trie {
public:
    TrieNode* root;
    
    Trie() {
        root = new TrieNode();
    }
    
    void insert(std::string word) {
        TrieNode* cur = root;
        for (char alphabet : word) {
            if (cur->children.find(alphabet) == cur->children.end()) {
                cur->children[alphabet] = new TrieNode();
            }
            cur = cur->children[alphabet];
        }
        cur->is_word_end = true;
    }
    
    bool search(std::string word) {
        TrieNode* cur = root;
        for (char alphabet : word) {
            if (cur->children.find(alphabet) == cur->children.end()) {
                return false;
            } else {
                cur = cur->children[alphabet];
            }
        }
        return cur->is_word_end;
    }
    
    bool startsWith(std::string prefix) {
        TrieNode* cur = root;
        for (char alphabet : prefix) {
            if (cur->children.find(alphabet) == cur->children.end()) {
                return false;
            }
            cur = cur->children[alphabet];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */