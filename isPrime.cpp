#include <cstdio>

bool isPrime(int num) {
    for (int i = 2; i < num; i++) {
        if (num % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int num;
    printf("Please enter your number: ");
    scanf("%d", &num);
    int * ptr = &num;

    if (isPrime(num)) {
        printf("YOur number is a prime number");
    } else {
        printf("Your number is not a prime number");
    }

}