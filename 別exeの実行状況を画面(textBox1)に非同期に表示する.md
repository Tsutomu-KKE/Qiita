```c#:C#
private IAsyncResult sr;
private Process pr = new Process();
private byte[] bb = new byte[4096];
private void callback(object o)
{
  int n = pr.StandardOutput.BaseStream.EndRead(sr);
  var s = Encoding.GetEncoding(932).GetString(bb, 0, n);
  textBox1.Text += s;
  textBox1.SelectionStart = textBox1.Text.Length - 1;
  textBox1.ScrollToCaret();
  if (n == 0) return;
  sr = pr.StandardOutput.BaseStream.BeginRead(bb, 0, bb.Length, callback, null);
}
private void button1_Click(object sender, EventArgs e)
{
  pr.StartInfo.FileName = XXX;
  pr.StartInfo.RedirectStandardOutput = true;
  pr.StartInfo.UseShellExecute = false;
  pr.Start();
  sr = pr.StandardOutput.BaseStream.BeginRead(bb, 0, bb.Length, callback, null);
  pr.WaitForExit();
}
```