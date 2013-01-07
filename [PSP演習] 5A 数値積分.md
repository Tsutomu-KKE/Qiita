次のような形式で、シンプソン則で積分する関数を作成せよ。

```c#
public delegate double CalcFunc(double x);
public static double Simpson(CalcFunc f, double lower, double upper);
```				
シンプソン則は、n 分割した n+1 個の位置での値に 1,4,2,4,2,...,1 を掛けて和をとり、 (upper-lower) を掛けて 3*n で割ったものが積分値となる。分割数は偶数でなければいけない。 無限ループにならないようにチェックせよ。