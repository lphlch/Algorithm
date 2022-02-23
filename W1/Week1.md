# 算法第一次作业

吕品灏 2052336

## 证明 $gcd(m,n)=gcd(n,m\ mod\ n)$

设 $m>n$ ， $m=kn+c$ ，其中 $k$ 为常数，$c=m\ mod\ n$ ，且 $c\not ={0}$，  
设 $p$ 为 $a,b$ 的一个公约数，将 $c=m-kn$ 两端同时除以 $p$ 之后，得：
$$\frac{c}{p}=\frac{m}{p}-\frac{kn}{p}$$
由等式右边可知， $\frac{c}{p}$ 也是一个整数，
因此， $p$ 是 $n,m\ mod\ n$ 的公约数。  
因其公约数相等，于是最大公约数也相等，得证。

## 计算 $\left\lfloor\sqrt n\right\rfloor$ 的算法  

## 证明主定理
设 $n$ 是 $b$ 的幂，令 $n=b^m$ ,并设 $f(1)=1 ，则
$$f\left(b^m\right)=af\left(b^{m-1}\right)+\left(b^k\right)^m$$
累加可得 
$$\frac{f\left(b^m\right)}{a^m}=\sum_{i=0}^{m}\left(\frac{b^k}{a}\right)^i$$
移项后，若 $a>b^k$ ，则
$$f(n)=O(a^m)=O(n^{log_ba})$$
若 $a=b^k$ ，则
$$f(n)=O(a^m{log_bn})=O(n^k{logn})$$
若 $a<b^k$ ，则  
$$f\left(n\right)=\frac{\left(\frac{b^k}{a}\right)^{m+1}-1}{\frac{b^k}{a}-1}=O\left(a^m\left(\frac{b^k}{a}\right)^m\right)=O\left(n^k\right)$$
得证。