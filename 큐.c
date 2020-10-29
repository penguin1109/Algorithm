//백준 10845번 큐
//배열 기반의 원형 큐로 구현

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define True 1
#define False 0
#define MAX 1000005

typedef struct queue{
    int arr[MAX];
    int head;
    int tail;
    int size;
}Queue;

void StartQueue(Queue *p){
    p -> size = 0;
    p -> head = 0;
    p -> tail = 0;
}

int GetNextIdx(int idx){
    if (idx + 1 >= MAX){
        return 0;
    }
    return idx + 1;
}

int SetNextIdx(int *idx){
    if ((*idx + 1) >= MAX){
        *idx = 0;
    }
    else (*idx)++;
}

int Empty(Queue *p){
    if (p -> head == p -> tail){
        return True;
    }
    else{
        return False;
    }
}

int Full(Queue *p){
    if (GetNextIdx(p->tail) == 0){
        return True;
    }
    return False;
}

int Front(Queue *p){
    if (Empty(p) == True){
        return -1;
    }
    return p -> arr[p->head];
}

int Back(Queue *p){
    if (Empty(p) == True){
        return -1;
    }
    return p-> arr[p->tail-1];
}

void Push(Queue *p, int data){
    if (Full(p) == True){
        return;
    }
    p->arr[p->tail] = data;
    SetNextIdx(&(p->tail));
    p->size ++;
}

int Pop(Queue *p){
    if (Empty(p) == True){
        return -1;
    }
    int data = p->arr[p->head];
    SetNextIdx(&(p->head));
    p->size --;
    return data;
}

int main(void){
    int n;
    scanf("%d", &n);
    char command[10];
    Queue q;
    StartQueue(&q);
    int data;

    for (int i = 0;i<n;i++){
        scanf("%s", command);

        if (!strcmp(command, "push")){
            scanf("%d", &data);
            Push(&q, data);
        }
        else if (!strcmp(command, "pop")){
            printf("%d\n", Pop(&q));
        }
        else if (!strcmp(command, "size")){
            printf("%d\n", q.size);
        }
        else if(!strcmp(command, "empty")){
            printf("%d\n", Empty(&q));
        }
        else if (!strcmp(command, "front")){
            printf("%d\n", Front(&q));
        }
        else if(!strcmp(command, "back")){
            printf("%d\n", Back(&q));
        }
    }
    return 0;
}