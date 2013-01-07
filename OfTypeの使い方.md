WindowsのFormの画面にCheckBoxがたくさんあるとします。
プログラムで、すべてチェック済みにしたいとき、

```c#:C#
foreach (var cntr in Controls)
{
	var cb = cntr as CheckBox;
	if (cb != null) cb.Checked = true;
}
```

このように書くと思いますが、OfTypeを使うと以下のようにかけます。

```c#:C#
foreach (var cb in Controls.OfType<CheckBox>()) cb.Checked = true;
```

似たようなものに Castがありますが、Castでは、型が異なると例外になります。
