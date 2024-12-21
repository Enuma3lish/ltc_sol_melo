#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies){
    int maxE = *max_element(candies.begin(), candies.end());
    vector<bool>res;
    for (auto can: candies){
        res.push_back(can+extraCandies>=maxE);
    }
    return res;
}
int main(){


}