

SELECT 
    DEPTNO as "부서번호",
    COUNT(EMPNO) as "근무자수",
    SUM(SAL) as "급여합"
FROM EMP
GROUP BY DEPTNO