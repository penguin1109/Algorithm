#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXLEN 100


typedef struct product{
    int pid;      //상품 번호
    char pName[MAXLEN];   //상품명
    int price;           //가격
    char store[MAXLEN];   //상품 보유 상점 이름
    int count;     //상품 재고 개수
}PRODUCT;

void getInventoryData(PRODUCT **arr, int size){
    for (int i = 0;i<size;i++){
        arr[i] = malloc(sizeof(PRODUCT));
        printf("상품 정보를 입력하시오 : ");
        scanf("%d %s %d %s %d", &(arr[i]->pid), &(arr[i]->pName), &(arr[i]->price), &(arr[i]->store), &(arr[i]->count));
    }
}

void storeForProduct(PRODUCT **ptr, const char *productName){
    for (int i=0;i<10;i++){
        if (strcmp(ptr[i]->pName, productName) == 0){
            printf("보유 상점 : %s  보유 개수 : %d\n", ptr[i]->store, ptr[i]->count);
        }
    }
}

int countNumStocks(PRODUCT **ptr, char *productName){
    int added = 0;
    for (int i=0;i<10;i++){
        if (strcmp(ptr[i]->pName, productName)==0){
            added = added + (ptr[i]->count);
        }
    }
    printf("%d\n", added);
}

void printProductList(PRODUCT **ptr){
    printf("상품번호  상품명  가격  상점  재고수");
    for (int i = 0;i<10;i++){
        printf("%3d %3s %3d %3s %3d", ptr[i]->pid, ptr[i]->pName, ptr[i]->price, ptr[i]->store, ptr[i]->count);
    }
}

int main(void){
    PRODUCT *arr[1000] = {NULL};
    int choice;
    char y_n;
    char prodName[MAXLEN];
    getInventoryData(arr, 10);
    printf("=====작업메뉴=====\n");
    printf("1. 특정 상품을 보유한 상점 및 상점 별 재고 개수 파악\n");
    printf("2. 특정 상품의 총 재고량 파악\n");
    printf("3. inventory list 출력\n");
    do{
        scanf("%d", &choice);
        getchar();
        switch(choice){
            case(1):
            printf("상품명을 입력하시오: ");
            gets(prodName);
            storeForProduct(arr, prodName);
            break;

            case(2):
            printf("상품명을 입력하시오: ");
            gets(prodName);
            countNumStocks(arr, prodName);
            break;

            case(3):
            printProductList(arr);
            break;
        }
        printf("계속 진행 하시겠습니까? : ");
        scanf("%c", &y_n);
    }while (y_n == 'y');
    return 0;
}