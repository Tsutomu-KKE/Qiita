下記の「TODO」を埋めて、リンクリストを完成させよ。

``` c#
public class MyLinkedList<T> : IEnumerable<T>
{
	internal class Item
	{
		internal T Value;
		internal Item Next;
		public Item(T t){ Value = t; }
	}
	public int Length { get; private set; }
	private Item Top;
	public MyLinkedList()
	{
		// TODO:初期化
	}
	public void AddLast(T t)
	{
		// TODO:追加
	}
	public IEnumerator<T> GetEnumerator()
	{
		// TODO:反復子
	}
	System.Collections.IEnumerator
		System.Collections.IEnumerable.GetEnumerator()
	{
		return GetEnumerator();
	}
}
```
