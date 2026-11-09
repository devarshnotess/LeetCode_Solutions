class Solution {
public:
    typedef pair<int, int> P;

    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
    
      
        set<int> free;

        priority_queue<P, vector<P>, greater<P>> busy; 

        vector<int> counts(k, 0);

    
        for(int server = 0; server < k; server++){
            free.insert(server);
        }

   
        int n = static_cast<int>(arrival.size());

        for(int i = 0; i < n; i++){

            int time = arrival[i];

       
            while(!busy.empty() && busy.top().first <= time){
                free.insert(busy.top().second);
                busy.pop();
            }

            
            if(free.empty()){
                continue;
            }

            auto it = free.lower_bound(i % k);

            if(it == free.end()){
                it = free.begin();
            }
             
            
            int server = *it;
            free.erase(it);

            counts[server]++;
            busy.emplace(time + load[i], server); 
        }


        int maxCount = *max_element(counts.begin(), counts.end());

        vector<int> ans;

        for(int server = 0; server < k; server++){

            if(counts[server] == maxCount){
                
                ans.push_back(server);
            }
        }
        
        return ans;

    }
};