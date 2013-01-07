以下のようにすれば、`(int)Some.CountOfSome`で項目数(=3)として使えます。
最初の要素はデフォルトで0なので、`=0`は不要ですが、数字に意味があるのを明示しています。

```c#:C#
enum Some
{
	A = 0,
	B,
	C,
	CountOfSome
}
```