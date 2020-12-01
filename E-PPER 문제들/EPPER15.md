### 3. 재고 없는 날
- 노트북이 하루에 한 개씩 판매가 되는데, 이때 현재 N개의 노트북을 가지고 있고 M일에 한 번씩 도매점으로부터 1개씩 입고가 된다.
- 노트북의 재고가 0이 될 때까지 며칠이 걸리는지 return 하는 solution 함수를 작성하시오. 
  - 단, 재고가 0이 될 때 도매점으로부터 입고되는 날이면 재고가 다시 1개 늘어난다.

```c
int solution(int n, int m){
    int answer = 1;
    while (n){
        if (answer % m != 0){
            n--;
        }
        answer ++;
    }
    return answer;
}

void main(void){
    int answer, n, m;
    scanf("%d %d", &n,&m);
    answer = solution(n,m);
    printf("%d", answer);
}
```

### 4. 100만들기
- 9개의 수가 담겨 있는 정수형 배열을 입력 받은 이후에 2개를 제외해서 7개의 정수의 합으로 100을 만들고자 한다.
- 이때 중요한 것은 정답으로 출력하게 될 문자 배열은 동적 메모리 할당 malloc를 사용해서 호출하는 것이기 떄문에 solution 함수의 출력값은 배열의 포인터, 즉 배열의 주소이다.
```c
int* solution(int numbers[9]){
    int *answer;
    answer = (int*)malloc(sizeof(int) * 7);

    int sum = 0;
    for (int i = 0;i<9;i++){
        sum += numbers[i];
    }
    int remove = sum-100;
    int i,j;
    for (int i = 0;i<9;i++){
        for (int j=i;j<9;j++){
            if (i!= j & numbers[i]+numbers[j] == remove){
                int idx = 0;
                for (int k = 0;k<9;k++){
                    if (k != i & k != j){
                        answer[idx] = numbers[k];
                        idx ++;
                    }
                }
            }
        }
    }
    return answer;
}

void main(void){
    int numbers[9] = {0};
    int* result;
    for (int i =0;i<9;i++){
        scanf("%d", &numbers[i]);
    }
    result = solution(numbers);
    for (int i =0;i<7;i++){
        printf("%d ", result[i]);
    }
}
```

### 5. 문자열 압축
- 문자열에 등장하는 문자의 종류가 한정되어 있는 경우에 연달아 들장하는 문자의 출현 횟수를 기록하는 방법으로 문자열의 저장에 소요되는 기억 공간을 줄인다.
```c
char* solution(char* s){
    char *answer = (char*)malloc(sizeof(char)*strlen(s));
    char temp = s[0];
    char alph = 'A';
    int idx=0;
    int i=0;
    while (i<strlen(s)){
        int count = 0;
        if (i == 0 & s[i] == '1'){
            answer[idx] = '1';
            idx++;
        }
        while (temp == s[i+count]){
            count++;
        }
        temp = s[i+count];
        i += count;
        answer[idx] = alph+count-1;
        idx++;
    }
    return answer;
}

void main(void){
    char src[MAXLEN];
    gets(src);
    char *pt = NULL;
    pt = solution(src);
    puts(pt);
}
```
- 이 문제도 마찬가지로 동적 할당 메모리 malloc를 사용하도록 하였으며, 문자열 비교를 할 때에 이 경우에는 각각의 문자배열이 아닌 그냥 문자를 비교하는 것이기 떄문에 ==를 사용하면 된다.
- 그리고 문자열을 출력하고자 할 떄에는 puts()를 사용하는 것이 특히 편리하다(공백이 없기 때문)
- 숫자데이터를 문자로 취급하는 것이 중요했다.

### 6. 후위 표기법
- 당연히 스택을 이용해서 해결하면 되는 문제라는 것은 보는 즉시 알 수 있었다.
- 사칙 연산의 우선순위를 고려해줄 필요는 없었기 때문에 순서대로 계산해 주면 되는 것이었고, 숫자면 stack에 넣고 연산자라면 pop을 수행해서 구했다.
  - 그러나 파이썬에는 이미 pop과 push등의 기능이 쉽게 가능한 반면에 c언어로 해결하려니 함수들을 직접 구현해야 한다는 불편함이 존재했다.

```c
//필요한 변수의 정의
int stack[10];
//스택의 제일 위에 있는 원소를 가리키는 포인터를 전역 변수로서 설정을 해 준다.
int top = -1;

//스택 연산에 필요한 함수 정의
//스택에서 계산하고자 하는 문자를 뽑아내는 pop
int pop(void){
    return stack[top--];
}
//스택에 숫자를 넣어주는 함수 push()
void push(int a, char* input){
    stack[++top] = input[a] - '0';
    //stack[++top]는 top++를 한 이후에 stack[top]를 하는 것과 동일하다.
}
//문자열에 대해서 후위 연산을 수행해주는 함수 cal()
int cal(int n, char* input){
    for (int i=0;i<n;i++){
        if (input[i] >= '0' && input[i] <= '9'){
            push(i, input);
        }
        else{
            switch(input[i]){
                case '+':
                stack[top] += pop();
                break;
                case '-':
                stack[top] -= pop();
                break;
                case '*':
                stack[top] *= pop();
                break;
                case '/':
                stack[top] /= pop();
                break;
            }
        }
    }
    return stack[0];
}

void main(void){
    int n, answer;
    scanf("%d", &n);
    char input[22];
    for (int i = 0;i<n;i++){
        scanf(" %c", &input[i]);
    }
    answer = cal(n, input);
    printf("%d", answer);
}
```

### 7. 도서관 예약
- 정렬을 구현하면서 해결해야 하는 문제였다.
- 학생들의 시작 시간과 종료 시간이 저장된 배열에서 종료 시간을 기준으로 오름차순으로 정렬하고 이때 시작시간이 같다면 시작 시간을 오름차순으로 정렬한다.
- 버블 정렬은 모든 자리에 대해서 각각 바로 다음의 수와 비교해 가며 맞는 자리를 찾아주는 정렬의 한 방법이다.
- 무조건 비어있는 자리가 둘중 하나라도 있다면 바로바로 학생을 채워 주어서 최대한으로 answer값을 크게 만드는 것이 목표이다.

```c
int solution(int s[], int slen, int e[], int elen){
    int answer = 0;
    int temp;
    int n = slen;
    //종료하는 시간을 기준으로 오름차순으로 정렬을 해줌
    //동시에 배열s도 일치하도록 맞추어서 순서를 바꾸어줌
    for (int i = 0;i<n;i++){
        for (int j = 0;j<n-1;j++){
            if ((e[j] > e[j+1])||(e[j] == e[j+1] && s[j] > s[j+1])){
                temp = e[j+1];
                e[j+1] = e[j];
                e[j] = temp;
                temp = s[j+1];
                s[j+1] = s[j];
                s[j] = temp;
            }
        }
    }
    //첫번째 좌석에 앚아 있는 학생의 종료 시점을 e1
    //두번쨰 좌석에 앉아 있는 학생의 종료 시점을 e2
    //위와 같이 설정하여 계속 시작 시점과 비교를 해 나간다.
    //greedy algorithm을 이용하는 방법으로 만약 앉을 수 있는 학생이 생긴다면 바로 앉히는 방법을 택한다.

    int e1=-1,e2=-1;

    for (int i = 0;i<n;i++){
        if (e1 <= s[i]){
            e1 = e[i];
            answer ++;
        }
        //e1를 먼저 검사하기 떄문에 만약에 e2의 자리가 비어 있다면 
        //e2를 검사한다는 것은 e1이 비어있지 않다는 의미이므로
        //e2에 e1의 자리를 할당해주고 e1에 새로운 e[i]를 할당한다.
        else if (e2 <= s[i]){
            e2 = e1;
            e1 = e[i];
            answer ++;
        }
    }
    return answer;
}

void main(void){
    int s[] = {0,6,3,1,1,2}, e[] = {3,7,10,5,9,8};
    int slen = 6, elen = 6;
    int answer = solution(s,slen,e,elen);
    printf("%d", answer);
}
```

### 8.e-Queen
- 기존의 n-Queen문제에 퀸이 들어갈 수 없는 자리만 추가해서 정보를 제공하였다.
- 따라서 가로 방향, 세로 방향, 윗대각선, 아랫대각선에 존재하는지의 여부와 더불어서 들어가면 안되는 자리인지까지에 대해서 파악해 준 뒤에 가능하고 모든 열을 다 돌았으면 정답 개수에 ++를 해주어서 답을 출력하면 된다.
- n의 크기가 14이하의 자연수로 지정이 되어 있기 때문에 초기에 데이터의(배열의) 크기 설정이 수월하다.
- 좌표가 어디서부터 (1,1)로 시작하는지를 제대로 파악하면 대각선 처리를 실수 없이 일차 함수의 관점에서 바라보면 할 수 있다.
```c
//해당 x행에 y번쨰 자리에 퀸의 존재 여부, 윗대각선에 존재 여부, 아래 대각선에 존재 여부확인
int check[14] = {0}, up[27] = {0}, down[27] = {0};
int N, count = 0;
int unable[14][14];
//n은 체스판의 크기 k는 절대 놓을 수 없는 위치의 개수
//n은 14이하의 자연수이고 k는 n이하의 자연수로 설정이 되어 있기 때문에 unable의 최대 크기를 14로 설정해야만 한다.
void eQueen(int idx){
    if (idx == N){
        count ++;
        return;
    }
    //각각의 idx번째 행의 n개의 열에 Queen이 들어가는경우를 모두 살펴봐야 한다.
    //대각선(위, 아래)모두 해당 경로에 다른 Queen이 존재하는지 확인
    //(idx, i)가 곧 (x, y)에 해당하는 좌표이다.
    for (int i = 0;i<N;i++){
        if ((unable[idx][i] == 0) && (check[i] == 0) && (up[i+idx] == 0) && (down[idx-i+13] == 0)){
        check[i] = 1;
        up[idx+i] = 1;
        down[idx-i+13] = 1;
        eQueen(idx+1);
        check[i] = 0;
        up[idx+i] = 0;
        down[idx-i+13] = 0;
        }
    }
}
int solution(int n, int k, int x[], size_t x_len, int y[], size_t y_len){
    int answer = 0;
    int i,j;
    N = n;
    for (int l = 0;l<k;l++){
        i = x[l];
        j = y[l];
        unable[i-1][j-1] = 1;
    }
    eQueen(0);
    answer = count;
    return answer;
}

void main(void){
    int n,k,a;
    scanf("%d, %d, ", &n, &k);
    //배열 입력을 위해서 malloc으로 동적 메모리를 할당해 주었다.
    int *x = (int*)malloc(sizeof(int) * k);
    int *y = (int*)malloc(sizeof(int) * k);
    scanf("[%d", &x[0]);
    for (int i = 1;i<k;i++){
        scanf(", %d", &x[i]);
    }
    scanf("] , [%d", &y[0]);
    for (int i = 1;i<k;i++){
        scanf(", %d", &y[i]);
    }
    scanf("]");
    a = solution(n,k,x,k,y,k);
    printf("%d", a);
    
    free(x);
    free(y);
}
```
**C로 문제를 풀 떄에도 Python으로 풀 떄와 마찬가지로 계속 사용해야 하는 데이터, 배열, 숫자, 정답값 등은 미리 정의해 주는 것이 훨씬 효율적이다. 굳이 main()함수 안에서 처리할 필요가 없다.**  


### 9. N개의 작업 공정
- 처음에는 문제에서 원하는 최솟값을 과연 어떻게 구할 수 있을 지에 초점을 맞추었는데 생각해 보니 그렇게 최솟값을 구하려 하지 않아도 어차피 선핼되는 공정이 끝나야만 수행을 할 수 있기 떄문에 값을 그렇게 계산하다 보면 나오는 결괏값이 곧 하나뿐인 걸리는 시간이자 최솟값이 될 것이다.
- 따라서 먼저 입력 받는 데이터 값들에 대해서 서로 선후 관계가 주어진 것은 2차원 배열에 넣고
- 재귀 함수를 이용해서 더이상 선행되는 공정이 없을 때 까지 진행을 값을 더해 나가도록 한다.
```c
//N_len은 배열 N의 길이이다.
//Relation_rows는 2차원 배열 Relation의 행 길이, Relation_cols는 2차원 배열 Relation의 열의 길이이다.
int answer = 0;
int N[100];

int linked[MAXSIZE][MAXSIZE] = {0};
int goal;

void find(int idx, int time){
    if (linked[idx][0] == 0){
        answer = time;
        return;
    }
    
    int temp=0, index = idx;
    int i=0;
    while (linked[idx][i] != 0){
        int node = linked[idx][i];
        if (temp < time + N[node-1]){
            temp = time + N[node-1];
            index = node;
        }
        i++;
    }
    find(index, temp);
}
int solution(int N[], size_t N_len, int **Relation, size_t Relation_rows, size_t Relation_cols, int goal){
    int a,b;
    for (int i = 0;i<Relation_rows;i++){
        int j = 0;
        a = Relation[i][0];
        b = Relation[i][1];
        if (linked[b][0] == 0){
            linked[b][0] = a;
        }
        else{
            while (linked[b][j] != 0){
                j++;
            }
            linked[b][j] = a;
        }
    }
    //linked에는 제대로 저장이 됨 (index 1 에서 n까지의 값들에 저장이 됨)
    find(goal, N[goal-1]);
    return answer;
}

void main(void){
    int n,r,goal;
    scanf("%d %d", &n, &r);
    getchar();
    for (int i = 0;i<n;i++){
        scanf("%d", &N[i]);
    }
    //2차원의 배열을 malloc을 이용해서 할당하기 위해서 사용하는 방법을 잠시 잊고 있었다.
    //그냥 1차원의 배열에 적용하는 방법과 달리 2차원이라면 처음에 이중 포인터를 사용해서
    //포인터들의 배열에 대한 포인터를 해야 하기 떄문에
    //제 1의 크기만큼 반복해서 포인터들의 배열에 제 2의 크기만큼 값들을 할당해 주어야 한다.
    int **Relation = malloc(sizeof(int*) * r);
    for (int i = 0;i<r;i++){
        Relation[i] = (int*)malloc(sizeof(int)*2);
    }
    for (int i = 0;i<r;i++){
        scanf("%d %d", &Relation[i][0], &Relation[i][1]);
    }
    scanf("%d", &goal);
    solution(N,n,Relation,r,2,goal);
    printf("%d", answer);
}
```
- 확실히 python으로 먼저 한번 풀어보고 이후에 c로 구현을 해보니까 코드를 구현하는데에 언어가 익숙하지 않아도 조금은 수월한 면이 존재헀다.


### 10. 랜덤 질문
- 한 교실에 기본 점수로 50점씩 모두 갖고 있는 학생 100명이 10x10의 형태로 반듯하게 앉아 있다.
- 교수들은 학생들 중 한 명씩 랜덤으로 선택하여 질문을 한다.
- 이때 학생이 정답을 말했을 경우에는 그 학생의 가로줄과 세로줄에 있는 모든 학생과 정답자 본인이 +1점을, 오답을 말했을 경우에는 -1점을 받는다.
- 제일 왼쪽 상단이 (1,1), 오른쪽 하단이 (10,10)이다.

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//우리가 malloc으로 동적 할당 메모리를 설정해 준 값은 포인터의 배열이다.
//즉, 포인터 값에 대한 배열이 또 2차원으로 구성이 되어 있다.
//따라서 pointer 구조형 정의를 (*point)[10]으로 바꾸어야
//동적 할당 메모리 answer 배열이 main함수에서 solution함수의 입력 인자로 인식이 된다.
int **solution(int (*point)[10], size_t point_rows, size_t point_cols){
    int** answer;
    answer = (int**)malloc(sizeof(int*)*10);
    int i,j,k;
    int temp,gap,gap2;
    int board[10][10];

    for (i = 0;i<10;i++){
        answer[i] = (int*)malloc(sizeof(int)*10);
        for (j = 0;j<10;j++){
            answer[i][j] = 2;
            board[i][j] = 50;
        }
    }

    for (i = 0;i<10;i++){
        for (j = 0;j<10;j++){
            temp = 0;
            for (k = 0;k<10;k++){
                temp += (point[i][k] + point[k][j]);
            }
            gap = temp - point[i][j];
            if (gap%2 != 0){
                answer[i][j] = 3;
                for (k = 0;k<10;k++){
                    board[i][k] ++;
                    board[k][j] ++;
                }
                board[i][j] --;
            }
        }
    }
    
    for (int i = 0;i<10;i++){
        for (int j = 0;j<10;j++){
            temp = 0;
            for (k = 0;k<10;k++){
                temp += (point[i][k] + point[k][j]);
            }
            gap = temp - point[i][j];
            temp = 0;
            for (k = 0;k<10;k++){
                temp += (board[i][k] + board[j][k]);
            }
            gap2 = temp - board[i][j];
            gap -= gap2;
            gap = gap%4 < 0 ? gap %4 +4 : gap % 4;
            if (gap == 2){
                answer[i][j] = 1;
            }
        }
    }
    return answer;
}

void main(void){
    int input[10][10];
    for (int i = 0;i<10;i++){
        for (int j = 0;j<10;j++)
            scanf("%d", &input[i][j]);
    }
    int** answer;
    answer = (int**)malloc(sizeof(int*)*10);
    answer = solution(input, 10,10);
    printf("\n");
    for (int i = 0;i<10;i++){
        for (int j = 0;j<10;j++){
            printf("%d ", answer[i][j]);
        }
        printf("\n");
    }
}
```
- 동적 메모리를 2차원 배열의 형태로 하고 함수의 입력 매개 변수와 선언 할때의 입력 값을 헷갈렸기 때문에 코드를 짜는 데에 상당한 시간이 걸렸다.
- 포인터 부분 공부를 좀 더 제대로 할 필요가 있음을 느꼈다.
- 만약에 위에 solution 함수에서 
```c
int** solution(int **point)
```
라고 선언하였다면 밑에 main함수에서도 인자를 이중 포인터로 만들었어야 했다. 따라서
```c
void main(void){
    int **input;
    input = (int**)malloc(sizeof(int*)*10);
    for (int i = 0;i<10;i++){
        input[i] = (int*)malloc(sizeof(int)*10);
    }
    answer = solution(input);
}
```
이렇게 했어야 했다.
**C언어는 특히 함수 선언과 정의 그리고 사용시에 입력 변수의 데이터형, 특히 포인터로 정의해야만 하는 배열의 경우 맞춰주는 것에 각별히 유의해야 한다.**