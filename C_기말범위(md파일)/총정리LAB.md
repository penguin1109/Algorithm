### 함수의 인자 전달
1. 실습1-2
- 함수의 인자로 정수의 포인터를 입력 받으면 해당 변수의 값 자체에 변화를 주고 싶을 때에는 간접 참조 연산자 * 를 사용해서 변화를 주어야 한다.
```c
void summation(int n, int *sum){
    for (int i = 0;i<=n;i++){
        *sum += i;
    }
}
```

2. 배열을 인자로 전달할 때에는 무조건 포인터를 이용한다.
 - ```int arr[]```이라고 인자 전달을 하는 것과 ```int *arr```이라고 하는 것은 동일하다.
 - ```int *arr```이라고 인자가 전달이 되면 배열의 값을 다루기 위해서는 ```*(arr+i)```이런 식으로 한다.
 - 만약에 배열의 시작이 아닌 중간부터 전달하고 싶다면 ```arr+i```의 형태로 인수에 입력하는 것이 가능하다.


3. 실습 4. 정수형 인자와 배열을 포인터로 전부 받아서 난수로 생성한 배열의 최대 최소 구하기
```c
void RnumberGen(int *A, int size, int range){
    int i;
    srand(time(NULL));
    for (i = 0;i<size;i++){
        A[i] = rand()%range+1;
    }
}

void GetMinMax(int *A, int size, int *min, int *max){
    *max = *A;
    *min = *A; 
    for (int i = 1;i<size;i++){
        *max = (*(A+i) > *max) ? *(A+i) : *max;
        *min = (*(A+i) < *min) ? *(A+i) : *min;
    }
}

int main(void){
    int A[10] = {0};
    RnumberGen(A, 10, 100);
    int min = 0, max = 0;
    GetMinMax(A, 10, &min, &max);
    printf("%d %d", min, max);
    return 0;
}
```

4. 실습 5
**확인해야 할 부분들**
- 역시나 다시 문자열의 처리가 헷갈렸다. 문자열의 일치 여부를 확인할 때는 무조건 ```strcmp() != 0```으로 확인하기 저렇게 0이 아닐동안에는 일치하지 않는다는 의미임 
- 문자열을 입력 받으면 어쨋든 문자들의 배열이기 떄문에 주소값이 입력이 된다. 따라서 ```*(arr+i)```와 ```arr[i]```는 동일하다.
- ```strlen()```은 문자열의 길이를 구해준다.(공백있는 문자열 말고 1차원 문자 배열만)
```c
void MakeUpper(char *arr, char *up){
    int count = 0;
    for (int i = 0;i<strlen(arr);i++){
        if (*(arr+i) >= 'a' && *(arr+i) <= 'z'){
            *(up+count) = *(arr+i) - 32;
            count ++;
        }
        else if (*(arr+i) >= 'A' && *(arr+i) <= 'Z'){
            *(up+count) = *(arr+i);
            count ++;
        }
    }
    up[strlen(arr)] = '\0';
}

void MakeLower(char *arr,char *down){
    int count = 0;
    for (int i = 0;i<strlen(arr);i++){
        if (*(arr+i) >= 'A' && *(arr+i) <= 'Z'){
            *(down+count) = *(arr+i) + 32;
            count ++;
        }
        else if (*(arr+i) >= 'a' && *(arr+i) <= 'z'){
            *(down+count) = *(arr+i);
            count ++;
        }
    }
    down[strlen(arr)] = '\0';
}

int main(void){
    char arr[MAXSIZE];
    printf("문자열을 입력하시오 : ");
    gets(arr);
    char up[MAXSIZE], down[MAXSIZE];
    while (strcmp(arr,"\0") != 0){
        MakeLower(arr, down);
        MakeUpper(arr, up);
        printf("Low : %s Up : %s\n", down, up);
        printf("문자열을 입력하시오 : ");
        scanf("%s", &arr);
        getchar();
    }
    return 0;
}
```

5. 실습7. 구조체의 연결 리스트 만들기
- ```strcmp() == 0```은 ```strcmp()```와 동일한 의미를 지닌다.
- ```NULL```은 integer이다. 상수이기 떄문에 ```"\0"```과 사실상 같은 의미를 지닌다.
```c
typedef struct data{
    char name[MAXSIZE];
    /*반드시 구조체의 포인터를 정의해 줄 때에는 ```struct 구조체명 *포인터명```이런식으로*/
    struct data *next;
}NameNode;

void MakeList(NameNode *n1, NameNode *n2, NameNode *n3, NameNode *n4, NameNode *n5){
    n1 -> next = n2;
    n2 -> next = n3;
    n3 -> next = n4;
    n4 -> next = n5;
}

void InsertNode(NameNode *n1, NameNode *n6){
    NameNode *p = n1, *p2;
    while (strcmp(p -> name, "Oh")){
        p = p->next;
    }
    p2 = p->next;
    p->next = n6;
    n6->next = p2;
}

void PrintList(NameNode *n1){
    NameNode *p;
    p = n1;
    while (p != NULL){
        printf("%s\n", p->name);
        p = p->next;
    }
}
int main(void){
    NameNode s1,s2,s3,s4,s5,s6;
    strcpy((s1.name), "Lim");
    s1.next = NULL;
    strcpy((s2.name), "Oh");
    s2.next = NULL;
    strcpy((s3.name), "Shim");
    s3.next = NULL;
    strcpy((s4.name), "Park");
    s4.next = NULL;
    strcpy((s5.name), "Yang");
    s5.next = NULL;
    strcpy((s6.name), "Jang");
    s6.next = NULL;

    MakeList(&s1, &s2, &s3, &s4, &s5);
    InsertNode(&s1, &s6);
    PrintList(&s1);
    return 0;
}
```

### 기억 부류 (Storage Class)
- 변수의 **저장 위치**와 **사용 범위**를 지정
1. auto 변수
   - 지역변수는 항상 auto 기억 부류로 사용
   - 전역변수에는 지정 불가
2. register 변수
   - 변수를 메모리에 할당하는 대신에 CPU의 register에 할당한다.
3. extern 변수
   - 프로그램 전체에서 유효하고 다른 파일에서도 참조 가능
   - 전역변수에 대한 extern 선언이 있으면 한 파일 내에서도 전역 변수가 선언된 위치에 관계없이 전역 변수 사용 가능
   - extern 선언을 굳이 따로 하지 않는다면 선언,즉 ```int global = 0```와 같이 선언한 위치 이후부터만 사용이 가능한 변수인 것이다.
   - 함수 밖에서 선언
  
4. static 변수(정적 변수)
   - 정적 지역 변수: 함수가 return하더라도 해제되지 않고 남아있다가 그 다음 함수가 호출 될 때 다시 이용
   - 선언된 함수 안에서만 사용 가능

5. static 변수(전역 변수)
   - 정적 전역 변수가 선언된 소스 파일에서만 사용할 수 있다.
   - 전역 변수를 다른 소스 파일에서 접근하지 못하도록 제한한다.

6. 함수의 범위
   - extern 선언으로 해당 함수를 다른 소스 파일에서 접근할 수 있도록 할 수 있다.
   - 정적 함수(Static 함수) : 함수가 정의된 소스 파일에서만 함수를 호출 할 수 있으며, 다른 소스 파일에서는 extern으로 호출이 불가능하다.

7. 실습7 - 정적 지역 변수 사용 연습
```c
char* MakeUpper(char *arr){
    int len = strlen(arr);
    int count = 0;
    static char Up[MAXSIZE];
    for (int i = 0;i<len;i++){
        if (arr[i] >= 'a' && arr[i] <= 'z'){
            Up[count] = arr[i] - 32;
        }
        else{
            Up[count] = arr[i];
        }
        count ++;
    }
    Up[count] = '\0';
    return Up;
}

int main(void){
    char y_n;
    char arr[MAXSIZE];
    do{
        printf("문자열을 입력하시오 : ");
        gets(arr);
        char *low = MakeLower(arr);
        char *up = MakeUpper(arr);
        printf("소문자 : %s 대문자 : %s ", low, up);
        printf("계속 진행 하겠습니까? : ");
        scanf("%c", &y_n);
        getchar();
    }while(y_n == 'y');
}
```
- 문자열, 문자 배열을 다룰 떄는 주소, 즉 포인터 값으로 인자를 입력하고 받아오는 것을 수행해야 한다.
- ```puts(p)```를 하면 문자열 p를 출력하게 된다.(p는 char형의 포인터)

8. (실습 9) - 전역 변수 사용 연습
- 아래와 같이 전역변수로 num, arr[MAXSIZE]를 선언해서 해당 소스 파일에서 선언 위치로부터 공유할 수 있도록 했다.
- 굳이 extern을 사용하지 않고도 함수 밖에서 변수를 선언하게 되면 해당 위치부터는 유효하다.
```c
int num = 0;
int arr[MAXSIZE];

void CountNum(){
    int pos=0, neg=0;
    for (int i = 0;i<num;i++){
        if (arr[i] > 0){
            pos++;
        }
        else if (arr[i] < 0){
            neg ++;
        }
    }
    printf("양수는 %d개, 음수는 %d개", pos, neg);
    //main함수에서 출력하고 싶다면 pos와 neg의 포인터 값을 CountNum의 입력 인수로 전달하는 방법도 존재
}
```

### 포인터의 활용
1. 포인터 배열 (배열의 원소를 가리키는 포인터)
   - 주소를 저장하는 배열을 선언한다. (```int *arr[5]```)
   - 즉, 포인터 배열의 각 요소들은 곧 다른 배열/요소의 주소인 것이다.
   - 포인터 배열의 각 원소에 배열의 시작 주소를 저장할 수 있다.
```c
void main(){
    int x[3] = {1,2,3};
    int y[3] = {4,5,6};
    int z[3] = {7,8,9};
    int *arr[] = {x,y,z};
}
```
    - 위와 같이 하면 ```arr[i][j]```라 할 때 ```arr[i]```는 int* 변수이고 ```arr[i][j]```는 int 변수이다.
    - ```*(arr[i] + j)```라 하면 ```arr[i]```는 역시나 int* 변수, ```*(arr[i]+j)```는 int 변수이다.

- 구조체 포인터 배열
```struct student* std[100];``` 이런 식으로 구조체 포인터 배열을 준비하고 구조체 변수가 필요할 때에 메모리에 할당하고 그 주소만 저장한다.

2. 배열에 대한 포인터 (2차원 배열)
    - 데이터형 (*포인터 명)[배열크기];
    - 위와 같은 형식을 띄는 포인터로, 배열 전체의 주소를 저장하는 포인터, 즉 주소를 저장하는 변수인 것이다.
      - 배열 전체의 주소를 구하기 위해서는 배열 이름 앞에 & 연산자로 지정을 하면 된다.
      - & 연산자 없이 배열 이름만 사용하면 배열의 첫번째 원소의 주소를 의미하기 때문이다.
      - 배열에 대한 포인터에는 크기가 같은 배열 주소만 저장이 가능하다.
    - p가 배열에 대한 포인터일 때 무조건 ```(*p)[i] == p[0][i]```이다.
```c
int arr[5] = {1,2,3,4,5};
int (*p)[5] = arr;
```
일 때 ```(*p)```는 크기가 5인 int형 배열 arr을 가리키고, ```(*p)[i]```는 int[5]배열의 i번째 원소를 의미한다.
```*((*(p)) + i) == (*p)[i] == p[0][i]```
- ```p``` : 크기가 5인 int 배열 arr의 주소
- ```*(p)``` : 크기가 5인 int 배열 arr 자체
- ```*(p) + i``` : 배열 arr의 i번째 요소의 주소
- ```*(*(p) + i)``` : arr[i], 즉 배열 arr의 i번째 요소

- `*p[i]`는 `p[i]`가 가리키는 값이라는 의미이고, `(*p)[i]`는 p가 가리키는 배열의 i번째 요소라는 뜻이다.

- 배열에 대한 포인터는 2차원 배열의 한 묶음을 가리키는데 쓰임
- 2차원 배열의 제2크기와 같게 배열의 크기를 지정해서 선언
- 2차원 배열의 시작 주소로 초기화
- 배열 arr의 제2크기가 5일때 `int *(p)[5] = arr`는 곧 `int *(p)[5] = &arr[0]`과 같은 의미이다.
- 배열에 대한 포인터를 증가시키면 2차원 배열의 제 2 크기만큼씩 포인터의 주소가 증가하게 된다.

3. (실습 3) - 포인터 배열을 파라미터로 받는 함수
```c
void f(int **p, int m, int n){
    for (int i = 0;i<m;i++){
        for (int j = 0;j<n;j++){
            printf("%d ", *((*(p+i))+j));
        }
        printf("\n");
    }
}
int main(void){
    int x[3] = {1,2,3};
    int y[3] = {4,5,6};
    int z[3] = {7,8,9};
    int k[3] = {10,11,12};
    //배열의 원소를 가리키는 포인터이기 때문에 주소를 저장하는 배열을 선언한다.
    //즉, 데이터형이 int*, 즉 int형의 포인터이고 4개의 주소가 저장된 크기 4의 배열인 것이다.
    int* p[4] = {x,y,z,k};
    f(p,4,3);
    return 0;
}
`
- 중요한 것은 이것이 2차원 배열이 아니라 배열의 원소를 가리키는 포인터 배열이라는 것이다. 
- f함수의 입력 인자로 입력할 때에 `int* *p`대신에 `int *p[]`라고 입력해도 된다. 

4. (실습 4) - 구조체 포인터 배열을 파라미터로 받는 함수
- 위에서 이용한 정수 배열과 마찬가지로 `struct student* std[]`로 입력 인자를 바꾸어도 상관이 없다.
- 함수에 입력이 되면 포인터로서 인식을 하기 때문에 sizeof(std)를 하면 포인터의 크기, 즉 4가 되기 떄문에 미리 구조체 포인터 배열의 크기또한 입력 인자로 전달해 주어야 한다.
`c
void compute_avg(struct student** std, int num){
    for (int i = 0;i<num;i++){
        int sum = 0;
        sum += std[i] -> korean + std[i]->english + std[i]->math;
        std[i]->average = (double)sum/3;
    }

}
int main(void){
    STUDENT s1 = {"Jihe", 100,100,100,0.0};
    STUDENT s2 = {"Eunji", 90,80,88,0.0};
    STUDENT s3 = {"Chayon", 45,32,44,0.0};
    STUDENT* std[3] = {&s1, &s2, &s3};
    int num = sizeof(std)/sizeof(std[0]);
    compute_avg(std, num);
    for (int i = 0;i<3;i++){
        printf("%lf ", std[i]->average);
    }
    return 0;
}
```

5. (실습 6)
- 2차원 배열 원소 접근을 위한 배열에 대한 포인터의 이용
- 배열에 대한 포인터는 배열 자체의 주소를 저장하게 된다.
```c
void add(int (*p)[5], int size1, int size2, int *sum){
    for (int i = 0;i<size1;i++){
        for (int j = 0;j<size2;j++){
            *sum += *((*(p+i))+j);
        }
    }
}
int main(void){
    int arr[3][5] = {{1,2,3,4,5}, {6,7,8,9,10},{11,12,13,14,15}};
    int (*p)[5] = arr;
    int sum = 0;
    add(p, 3,5,&sum);//add(arr, 3,5,&sum)으로 그냥 포인터 대신 2차원 배열명을 그대로 입력해도 무방하다.
    printf("%d", sum);
    return 0;
}
`

- 그리고 함수에 변수 입력할 떄에 변수의 데이터형을 반드시 기재해 주어야 한다.
- ```arr[i][j]``` = ```*(arr[i]+j)``` = ```*((*(arr+i))+j)``` = ```(*(arr+i))[j]```
```c
typedef struct student{
    char name[20];
    int korean, english, math;
    double average;
}STUDENT;

void GetAvgOfClass(int (*arr1)[10], int size1, int size2, int *arr2){
    for (int i = 0;i<size1;i++){
        int sum = 0;
        for (int j = 0;j<size2;j++){
            sum += *(arr1[i]+j);
        }
        arr2[i] = sum/size2;
    }
}

void PrintArray1(int *arr, int size){
    for (int i = 0;i<size;i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void PrintArray2(int(*arr)[10], int size1, int size2){
    for (int i = 0;i<size1;i++){
        for (int j = 0;j<size2;j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

int main(void){
    int std_score[3][10];
    int class_score[3];
    srand(time(NULL));
    for (int i = 0;i<3;i++){
        for (int j=0;j<10;j++){
            std_score[i][j] = rand()%101;
        }
    }
    GetAvgOfClass(std_score, 3,10, class_score);
    PrintArray2(std_score, 3,10);
    PrintArray1(class_score, 3);
    return 0;
}
```

### 동적 메모리
- 배열의 크기를 미리 알 수 없을 때 배열의 크기는 변수로 지정할 수 없다.
- malloc 함수의 원형
```c
void *malloc(size_t size);
int *arr = NULL;
arr = malloc(sizeof(int) * size);
```
  - size : 할당할 메모리의 바이트 크기
  - return 값 : 할당된 메모리의 주소(void*형) -> 특정 포인터형 변수에 저장함
  - 동적 메모리를 할당할 수 없으면 NULL return
- free 함수의 원형
```c
void free(void* memblock);
free(arr);
arr = NULL;
```
  - memblock : 해제될 메모리의 주소
  - 인자로 넘겨준 포인터가 가리키는 동적 메모리를 해제한 이후에 NULL값을 할당해 준다.

- 동적 메모리를 구조체에 대해서 할당하고 싶을 때에는 
```c
typedef struct rect{
    int x,y;
    int width, height;
}RECT;
RECT* arr[100];
for (int i = 0;i<3;i++){
    arr[i] = malloc(sizeof(RECT));
}
```
이런 식으로 필요할 때마다 동적 메모리에 할당하고 그 주소만 포인터 배열의 원소로 저장하게 된다.
- arr[i]는 구조체 포인터이기 때문에 구조체의 멤버에 접근할 때 -> 연산자를 사용한다.


2. (실습 1) - 함수의 활용
```c
void PrintArray(int *A, int size){
    for (int i = 0;i<size;i++){
        printf("%d ", A[i]);
    }
}
int main(){
    int size = 5;
    //동적 메모리의 주소를 저장할 포인터 A를 선언
    int *A = NULL;
    int i, sum = 0;
    A = (int*)malloc(sizeof(int)*size);
    SaveArray(A, size);
    PrintArray(A, size);
    free(A);
    return 0;
}
```


3. 2차원 배열의 동적 메모리와 1차원 배열의 동적 메모리
```c
int **A = (int**)malloc(sizeof(int*)*n);
for (int i = 0;i<n;i++){
    A[i] = (int*)malloc(sizeof(int)*m);
}
int *B = (int*)malloc(sizeof(int)*n);
```    

4. 구조체의 크기를 모를 때에 구조체 포인터의 동적 메모리
- 구조체 포인터 배열은, 즉 동적 메모리로 할당해 주는 모든 포인터 배열들은 이중 포인터의 개념으로 생각하면 된다.
- 특히 구조체 포인터 배열의 경우 반복적으로 할당해 주어야 한다.
```c
typedef struct student{
    char name[20];
    int korean, english, math;
}STUDENT;

void Cal(STUDENT** arr, int n){
    for (int i = 0;i<n;i++){
        int score = 0;
        score += arr[i]->korean+arr[i]->english+arr[i]->math;
        printf("%s의 평균은 %d이다.", arr[i]->name, score/3);
    }
}
int main(void){
    char y_n;
    STUDENT* arr[100];
    int i = 0;
    do{
        arr[i] = (STUDENT*)malloc(sizeof(STUDENT));
        printf("학생 이름을 입력하시오 : ");
        scanf("%s", &arr[i]->name);
        printf("학생 성적을 입력하시오 : ");
        scanf("%d %d %d", &(arr[i]->korean), &(arr[i]->english), &(arr[i]->math));
        i++;
        printf("더 입력할 학생 정보가 있나요? : ");
        fflush(stdin);
        scanf("%c", &y_n);
    }while (y_n == 'y');
    Cal(arr, i);
}
```
- 구조체 포인터 배열을 이용한 동적 메모리 할당을 할 때에 함수의 입력 인자로 `STUDENT* std[]`또는 `STUDENT* *std`모두 가능하다.
- `fflush(stdin)`은 %c형태를 입력 받을 때 생기는 enter와 같은 입력 버퍼를 제거해 준다.

### 입출력 라이브러리
1. stream과 표준 입출력
- stream은 연속된 데이터 바이트의 흐름이다.
- stream 기반의 입출력은 buffer을 경유한 입출력으로 수행이 된다.
- 입력 : 키보드로부터 입력된 내용을 임시로 버퍼에 저장했다가 특정 시점(읽기 명령 수행 시)에 프로그램으로 전닫한다.
  **scanf()와 %d**
  - %d는 leading 공백 문자를 skip 한 이후에 flush 하는 작용을 수행한다. 즉, 앞에 엔터와 같은 버퍼 문자가 남아 있는 것은 상관이 없다.
  - 이는 공백 문자를 숫자의 끝으로 인식하기 떄문이다.
  - 그리고 ending 공백 문자는 그냥 leave하게 된다.

2. 파일 입출력
  1. 파일 열기
    - `fopen()`함수를 호출해서 파일을 열어야 한다.
    - `FILE* fopen(char* filename, char* mode)`와 같이 fopen()의 파라미터로 파일명과 파일 열기 모드를 지정하면 해당 파일에 대한 파일 stream을 생성하고, 생성된 파일 stream에 대한 파일 pointer을 return 하게 된다.
    - `r`:입력용 파일을 연다 `w`:출력용 파일을 연다. `b`:binary mode로 파일의 입출력을 수행한다
  2. 파일 닫기
   - `fclose()`함수를 호출해서 파일을 닫아야 한다.
   - `int fclose(FILE* stream)`와 같이 fclose()의 파라미터로 파일 포인터를 지정한다.
 3. 에러 확인
  - `ferror()`함수를 호출해서 파일 입출력시 발생하는 에러를 확인한다.
  - 에러 발생시 0이 아닌 값을 return 하고, 에러가 발생하지 않았으면 0을 return 한다.
 4. 파일의 끝인지 검사
  - `feof()`함수를 호출해서 파일의 끝인지를 검사한다.
  - 끝이면 0이 아닌 값을 return 하고, 끝이 아니면 0을 return 한다.


3. 텍스트 파일 입출력
  1. `int fgetc(FILE* f)`
   - 파일에서 한 문자를 입력받는다.
  2. `char* fgets(char* str, int n, FILE* stream);`
   - 파일에서 한 줄의 문자열을 입력받는다.
  3. `int fputs(char* str, FILE* f)`
   - 파일로 한 줄의 문자열을 출력한다.
  4. `int fscanf(FILE* f, char* format)`
   - 형식 문자열을 이용해서 파일에서 입력받는다.
  5. `int fprintf(FILE* f, char* format)`
   - 형식 문자열을 이용해서 파일로 출력한다.
  6. `int fputc(int c,FILE* f)`
   - 하나의 문자를 현재 위치의 화면에 출력한다.

```c
int main(void){
    FILE* f = NULL;
    FILE* f2 = NULL;
    int a;
    f = fopen("infile.txt", "r");
    f2 = fopen("outfile.txt", "w");
    //infile.txt에서 문자를 입력받음
    fscanf(f, "%d", &a);
    //outfile.txt로 문자를 출력함
    fprintf(f2, "a = %d", a);
    return 0;
}
```

4. 바이너리 파일의 입출력
- 중간중간 발생하는 결과들을 변수, 즉 메모리에 저장하게 되는데, 이때 메모리 부족을 막기 위해서 새로운 파일에 중간 결과를 입출력할 수 있도록 해준다.
- `fread()`, `fwrite()`함수를 이용한다.
```c
int main(void){
    int arr1[10] = {1,2,3,4,5,6,7,8,9,10};
    int arr2[10];
    int i;
    //파일용 포인터이기 때문에 파일의 주소를 반환하는 fopen()함수의 반환값을 포인터 변수에 할당해 준다.
    FILE* f;
    //binary 출력용으로 파일 열기
    f = fopen("test.dat", "wb");
    if (f == NULL){
        printf("파일 열기 실패\n");
        return -1;
    }
    fwrite(arr1, sizeof(int), 10, f);
    fclose(f);
    //test.dat라는 파일을 binary 읽기로 열기
    f = fopen("test.dat", "rb");
    //arr2[10] 배열에 정수 10개가 들어있는 배열을 f가 가리키는 파일에서 읽어 저장한다.
    fread(arr2, sizeof(int), 10, f);
    fclose(f);
    for (int i = 0;i<10;i++){
        printf("%d ", arr2[i]);
    }
    return 0;
}
```

5. (실습2) - 파일 모두 읽기
- 파일에 데이터가 더이상 없을 때까지 입력 받기 위해서는
```c
int main(void){
    FILE* f = NULL;
    f = fopen("infile.txt", "r");
    f2 = fopen("result.txt", "w");
    int a;
    while (!feof(f)){
        fscanf(f, "%d", &a);
        printf("a = %d\n", a);
        //새로운 txt파일인 result.txt에 그대로 출력한다.
        fprintf(f2, "result.txt", a);
    }
}
```
위와 같이 while문을 사용해 주면 된다. feof()는 끝이 아니면 0이 아닌 값을 반환한다.
```c
STUDENT arr[3] = {{"jihe", 10},{"uzi", 20},{"qwee", 30}};
    FILE* fp;
    fp = fopen("student.dat", "wb");
    fwrite(arr, sizeof(STUDENT), 3, fp);
    fclose(fp);
    fp = fopen("student.dat", "rb");
    STUDENT arr2[3];
    fread(arr2, sizeof(STUDENT), 3, fp);
    fclose(fp);
```
- 구조체를 이용해서 파일에 입출력을 할 때에도 동일하게 하지만, 구조체 자체로 입출력을 하려는 것이기 때문에 `sizeof(구조체 이름)`으로 실행한다.  

- binary file의 형태로 읽는 것이 아닐 때에는 반드시 `fscanf`로 파일의 내용을 읽고 `fprintf`로 파일에 내용을 출력할 수 있도록 하자.
- binary file일 경우에는 `fread`와 `fwrite`를 사용한다.
```c
int main(void){
    SCORE s1[10], s2[10];
    char name[20];
    int korean, english, math;
    FILE* fp = NULL;
    FILE* fp2 = NULL;
    int count = 0;
    fp = fopen("scores.txt", "r");
    fp2 = fopen("grade.dat", "wb");
    while (!feof(fp)){
        fscanf(fp, "%s %d %d %d", &(s1[count].name), &(s1[count].korean), &(s1[count].english), &(s1[count].math));
        count ++;
    }
    //fp에 의해서 s1에 저장한 정보를 grade.dat에 저장한다.
    fwrite(s1, sizeof(SCORE), 10, fp2);
    fclose(fp);
    fclose(fp2);
    fp2 = fopen("grade.dat", "rb");
    //크기가 10인 구조체 배열 s2가 10개의 SCORE 데이터형을 가진 구조체로 구성되었음을 파라미터로 전달하면서
    //grade.dat에 저장된 정보를 구조체에 저장한다.
    fread(s2, sizeof(SCORE), 10, fp2);
    fclose(fp2);
}
```

### 고급 기능
1. 분할 컴파일
- 헤더 파일: 서로 다른 소스 파일 사이에서 필요한 정보를 공유할 수 있도록 해준다.
  - 소스 파일에 정의된 함수나 전역 변수를 사용하는데에 필요한 정보를 제공한다.
  - 소스 파일에 헤더 파일을 포함하기 위해서는 #include를 사용한다.
  - 전처리기는 헤더 파일을 소스 파일이 존재하는 directory에서 찾는다.

2. 다른 파일에 정의된 함수의 호출
 - 다른 파일에 정의된 함수를 사용하려면 함수의 선언이 반드시 필요
 - 따라서 헤더 파일을 이용해서 함수의 선언을 한 곳에 모아 둘 수 있다.
 - 특정 소스 파일에 대한 헤더 파일을 만들고 나면, 소스 파일에도 자기 자신의 헤더 파일을 포함해 주는 것이 좋다. (즉, Array.c에도 Array.h를 포함 시키라는 의미)

3. 메크로, 구조체, typedef의 공유
 - 매크로, 구조체, typedef의 정의는 소스파일마다 필요하기 때문에 헤더 파일에 넣어준다.
 - 헤더 파일에 구조체나 typedef를 사용하는 함수의 선언이 들어갈 때는 구조체나 typedef의 정의 다음에 함수의 선언을 한다.

```c
/*Point.h*/
struct point{
    char name[10];
    int x,y;
}
typedef struct point POINT;
void PrintPoint(const POINT* p);
void MovePoint(const POINT* p, int dx, int dy);
```
- 위와 같은 방법으로 저장이 가능하다.

4. 다른 소스 파일에 선언된 전역 변수의 사용
- 전역변수의 extern 선언을 헤더 파일에 넣어준다.
- 전역변수는 프로그램 전체에서 반드시 하나의 소스 파일에 선언한다.
- 전역변수의 extern 선언은 메모리를 할당하지 않고, 전역변수의 데이터형과 변수명만 알려준다.
- 전역변수를 사용하려면 전역변수의 extern 선언이 들어 있는 header 파일을 포함시켜야 한다.

```c
/*Point.h*/
struct point{
    int x,y;
}
typedef struct point POINT;
void PrintPoint(const POINT* p);
extern POINT point_h;

/*Point.c*/
#include <stdio.h>
#include "point.h"
POINT point_h;
void PrintPoint(const POINT* p){
    printf("x : %d y : %d", p->x, p->y);
}

/*Main.c*/
#include <stdio.h>
#include "point.h"
void PrintPoint(&point_h);
```
- 위와 같은 방법으로 extern 전역 변수와 typedef, 그리고 다른 소스 파일에서 정의한 함수를 다른 소스 파일에서 이용하는 것이 가능하다.


4. 헤더 파일의 중복 피하기
  - 헤더 파일의 시작과 끝에 `#indef`, `#define`, `#endif`를 넣어준다.
  - `#indef`나  `#define`에 헤더 파일의 포함 여부를 알려주는 메크로 심볼을 지정한다.
```c
/*Point.h*/
#ifndef POINT_H
#define POINT_H

struct point{
    int x,y;
}
typedef point POINT;
void PrintPoint(const POINT* p);
extern POINT g_origin;
#endif
```
- 위와 같은 방법으로 헤더 파일의 시작과 끝에 해당 파일이 포함이 되어 있으면 사용하고 아니면 무시하도록 한다.

5. 헤더 파일과 소스 파일의 구성
```c
/*Module.h*/
#indef MODULE_H
#define MODULE_H

메크로 정의
구조체 정의 
typedef 정의
함수 선언
전역변수의 extern 선언

#endif

/*Module.c*/
#include <library header>
#include "사용자 정의 헤더"

함수 정의

전역 변수의 선언(전역 변수의 메모리 할당)
```
- `#if` `#else` `#endif`라는 전처리기를 사용해서 조건에 따라 컴파일 할 수 있는 방법도 존재한다.

6. 여러개의 소스 파일을 링크 시키는 방법
    1. main.c : main함수가 있는 파일로 다른 두개의 소스 파일의 함수 호출
    2. getsum.c : `int GetSum(int num);`정의
    3. print.c : `void PrintResult(int num, int res);`정의
    4. getsum.h : getsum.c에 정의된 함수를 선언
    5. print.h : print.c.에 정의된 함수를 선언

7. 명령행 인자를 사용해서 실행하기
  - 명령행 인자란 main 함수로 전달되는 command-line parameter이다.
  - 이는 프로그램을 실행할 때에 지정이 된다.
```c
int main(int argc, char* argv[]);
```
- argc는 명령행 인자의 개수이고 argv는 명령행 인자로 전달된 문자열의 배열이다.
- `atoi()`는 문자열을 정수로 바꾸어주는 `<stdlib.h>`에 들어있는 내장형 함수이다.
- `atof()`는 문자열을 실수로 바꾸어 주는 내장형 함수이다.

```c
int main(int argc, char* argv[]) {
	int add = 0;
	for (int i = 1; i < argc; i++) {
		add += atoi(argv[i]);
	}
	printf("%d", add);
	return 0;
}
```
- 위와 같이 main()함수의 파라미터를 설정해서 visual studio내에서 속성을 변경해서 구해준다.
- 아래와 같이 임의의 영문 문서를 저장하고 있는 파일명과 -p, -u, -l중 하나를 명령행 인자로 받아서 요구되는 작업을 수행하도록 할 때에 명령행 인자의 두번째 문자열부터 이용을해서 인식을 해 주어야 한다.

```c
int main(int argc, char* argv[]) {
	FILE* fp2 = NULL;
	fp2 = fopen(argv[1], "r");

	char temp[MAXLEN];
	char A[MAXLEN][MAXLEN];
	int count = 0;

	if (!strcmp(argv[2], "-u")) {
		while (!feof(fp2)) {
			fscanf(fp2, "%s", temp);
			for (int i = 0; i < strlen(temp); i++) {
				if (temp[i] >= 'a' && temp[i] <= 'z') {
					temp[i] -= 32;
				}
			}
			printf("%s ", temp);
		}
		printf("\n");
	}
	else if (!strcmp(argv[2], "-p")) {
		while (!feof(fp2)) {
			fscanf(fp2, "%s", temp);
			strcpy(A[count], temp);
			count++;
		}
		for (int i = 0; i < count; i++) {
			printf("%s ", A[i]);
		}
		printf("\n");
	}
	else if(!strcmp(argv[2], "-l")) {
		while (!feof(fp2)) {
			fscanf(fp2, "%s", temp);
			for (int i = 0; i < strlen(temp); i++) {
				if (temp[i] >= 'A' && temp[i] <= 'Z') {
					temp[i] += 32;
				}
			}
			printf("%s ", temp);
		}
		printf("\n");
	}
}
```