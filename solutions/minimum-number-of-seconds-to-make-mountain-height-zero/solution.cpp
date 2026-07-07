// class Solution {
// public:
//     bool canFinish(long long time, int mountainHeight, vector<int>& workerTimes) {
//         long long total = 0;

//         for (int t : workerTimes) {
//             long long unit = 1;

//             while ((long long)t * (unit * (unit + 1) / 2) <= time) {
//                 unit++;
//             }

//             total += (unit - 1);

//             if (total >= mountainHeight)
//                 return true;
//         }

//         return false;
//     }

//     long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
//         long long low = 1;
//         long long high = 1e15;
//         long long ans = high;

//         while (low <= high) {
//             long long mid = low + (high - low) / 2;

//             if (canFinish(mid, mountainHeight, workerTimes)) {
//                 ans = mid;
//                 high = mid - 1;
//             } else {
//                 low = mid + 1;
//             }
//         }

//         return ans;
//     }
// };

// TLE CODE



class Solution {
public:

    bool canFinish(long long time, int mountainHeight, vector<int>& workerTimes) {
        long long total = 0;

        for (int t : workerTimes) {

            long long X = (2LL * time) / t;

            long long k = (sqrt(1.0 + 4.0 * X) - 1) / 2;

            total += k;

            if (total >= mountainHeight)
                return true;
        }

        return false;
    }

    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {

        long long low = 1;
        long long high = 1e18;
        long long ans = high;

        while (low <= high) {

            long long mid = low + (high - low) / 2;

            if (canFinish(mid, mountainHeight, workerTimes)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }
};