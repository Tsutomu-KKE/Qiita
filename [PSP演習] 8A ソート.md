マージソートで安定ソートせよ。

```c#
public static void Sort<T>(IList<T> a, Comparison<T> f) { Sort<T>(a, f, 0, a.Count); }
public static void Sort<T>(IList<T> a, Comparison<T> f, int i, int j);
```