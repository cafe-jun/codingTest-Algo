

SELECT 
    DEPTNO as "부서번호",
    DEPT."부서명" as "부서명"
    COUNT(EMPNO) as "근무자수",
    SUM(SAL) as "급여합"
FROM EMP
INNER JOIN DEPT
ON DEPT.DEPTNO = EMP.DEPTNO
GROUP BY EMP.DEPTNO