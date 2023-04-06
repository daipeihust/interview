#include <stdio.h>

int main() {
    int p1 = 0;
    int p2 = 0;
    int *arr1;
    int *arr2;
    int *result = malloc();
    sort(arr1);
    sort(arr2);
    while (p1 < len(arr1) && p2 < len(arr2)) {
        if (arr1[p1] > arr2[p2]) {
            p2++;
            continue;
        } else if (arr1[p1] == arr2[p2]) {
            insert(result, arr1[p1]);
            p2++;
        }
        p1++;
    }
    // 打印结果
    for (int i = 0; i < len(result); i++) {
        print("%d", result[i]);
    }
    return 0;
}