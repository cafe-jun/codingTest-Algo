void swap(int *p, int *q)
{
    int temp;
    // p가 가리키는 값을 임시 변수 temp 저장.
    temp = *p;
    // p가 가리키는 곳에 q의 값을 저장
    *p = *q;
    // q가 가리키는 곳에 임시 변수 temp의 값을 저장
    *q = temp;
}