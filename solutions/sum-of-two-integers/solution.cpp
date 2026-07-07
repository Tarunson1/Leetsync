class Solution {
public:
    int add(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }

    int getSum(int a, int b) {
        return add(a, b);
    }
};