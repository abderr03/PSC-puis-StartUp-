using System.Diagnostics;

class Test {
  static void run_cmd(string cmd, string args)
  {
      ProcessStartInfo start = new ProcessStartInfo();
      start.FileName = "python3";
      start.Arguments = string.Format("{0} {1}", cmd, args);
      start.UseShellExecute = false;
      start.RedirectStandardOutput = true;
      using(Process process = Process.Start(start))
      {
          using(StreamReader reader = process.StandardOutput)
          {
              string result = reader.ReadToEnd();
              Console.Write(result);
          }
      }
  }

  static void Main(string[] args) {
	run_cmd("test.py", "\"bonjour je suis présent !\"");
  }
}
