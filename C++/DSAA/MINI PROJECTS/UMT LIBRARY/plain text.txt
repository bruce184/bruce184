#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

struct Node{
    string key;
    string value;
    Node *next;
    Node(const string &k, const string &v): key(k), value(v), next(nullptr){}
};

class LRUCache{
private:
    int capacity;
    int size_;
    Node *head;
    Node *tail;
    unordered_map<string, Node*> cache;

    void remove_node(Node *node){
        if (head == node){
            head = head -> next;
            if (head == nullptr){
                tail = nullptr;
            }
        }else {
            Node *current = head;
            while (current -> next != node){
                current = current -> next;
            }
            current -> next = node -> next;
            if (node == tail){
                tail = current;
            }
        }
        cache.erase(node -> key);
        delete node;
        size_--;
    }

    void add_node_to_head(Node *node){
        node -> next = head;
        head = node;
        if (! tail){
            tail = node;
        }
        cache[node -> key] = node;
        size_++;
    }

    void move_to_head(Node *node){
        if (head == node) return;
        remove_node(node);
        add_node_to_head(node);
    }

public:
    LRUCache(int cap): capacity(cap), size_(0), head(nullptr), tail(nullptr){}

    string get(const string &key){
        if (cache.find(key) != cache.end()){
            Node *node = cache[key];
            move_to_head(node);
            return node -> value;
        }
        return "";
    }

    void set_(const string &key, const string &value){
        if (cache.find(key) != cache.end()){
            Node *node = cache[key];
            node -> value = value;
            move_to_head(node);
        }else {
            if (size_ >= capacity){
                remove_node(tail);
            }
            Node *new_node = new Node(key, value);
            add_node_to_head(new_node);
        }
    }

    int current_size() const{
        return size_;
    }

    void print_cache() const{
        Node *current = head;
        while (current){
            cout<<current -> key<<": "<<current -> value<<" -> ";
            current = current -> next;
        }
        cout<<"None"<<endl;
    }

    ~LRUCache(){
        Node *current = head;
        while (current){
            Node *next_node = current -> next;
            delete current;
            current = next_node;
        }
    }
};

int main(){
    // Add 3 books to the cache
    LRUCache lru_cache(3);
    lru_cache.set_("Book 1", "Beauty and the Beast");
    lru_cache.set_("Book 2", "Harry Potter");
    lru_cache.set_("Book 3", "After");
    cout<<"Cache after adding 3 books: "<<endl;
    lru_cache.print_cache();

    // Access Book 1 to make it most recently used
    cout<<"Accessing Book 1:"<<endl;
    cout<<"Value: "<<lru_cache.get("Book 1")<<endl;
    lru_cache.print_cache();

    // Add a new book -> remove the least recently used book (Book 2)
    cout<<"Adding Book 4 -> remove the least recently used book (Book 2):"<<endl;
    lru_cache.set_("Book 4", "The Summer I Turned Pretty");
    lru_cache.print_cache();

    // check the current size
    cout<<"Current size: "<<lru_cache.current_size()<<endl;

    return 0;
}

