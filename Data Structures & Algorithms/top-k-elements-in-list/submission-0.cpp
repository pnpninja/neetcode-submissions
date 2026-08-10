class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> numToCount;
        for(int num : nums){
            if(numToCount.find(num) == numToCount.end()){
                numToCount[num] = 1;
            }else{
                numToCount[num] = numToCount[num]+1;
            }
        }

        auto cmp = [](const pair<int, int>& a, const pair<int, int>& b){
            if(a.second != b.second){
                return a.second > b.second;
            }
            return a.first > b.first;
        };
        priority_queue<pair<int,int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);

        for (const auto& [num, count] : numToCount){
            if(pq.size() < k){
                pq.push({num, count});
            }else if(pq.top().second < count){
                pq.pop();
                pq.push({num, count});
            }
        }

        vector<int> ans(pq.size());
        int i = 0;
        while(!pq.empty()){
            ans[i] = pq.top().first;
            i++;
            pq.pop();
        }
        return ans;
    }
};