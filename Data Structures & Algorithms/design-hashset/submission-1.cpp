class Bucket{
    private:
        vector<int> numsInBucket;
    public:
        Bucket(){

        }
        void add(int key){
            auto pos = lower_bound(numsInBucket.begin(), numsInBucket.end(), key);
            if(pos != numsInBucket.end() && *pos == key){
                return;
            }
            numsInBucket.insert(pos, key);
        }

        void remove(int key) {
            auto pos = lower_bound(numsInBucket.begin(), numsInBucket.end(), key);
            if(pos != numsInBucket.end() && *pos == key){
                numsInBucket.erase(pos);
            }
        }

        bool contains(int key) {
            auto pos = lower_bound(numsInBucket.begin(), numsInBucket.end(), key);
            return pos != numsInBucket.end() && *pos == key;
        }
};

class MyHashSet {
    vector<Bucket> buckets;
public:
    MyHashSet() {
        buckets = vector<Bucket>(3000);
    }
    
    void add(int key) {
        int hash = key % 3000;
        buckets[hash].add(key);
    }
    
    void remove(int key) {
        int hash = key % 3000;
        buckets[hash].remove(key);
    }
    
    bool contains(int key) {
        int hash = key % 3000;
        return buckets[hash].contains(key);
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */