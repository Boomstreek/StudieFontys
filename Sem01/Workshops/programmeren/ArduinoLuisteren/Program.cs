using System;
using System.IO.Ports;
using System.Text.RegularExpressions;

class Program {
  static void Main() {
    string portName = "/dev/ttyUSB0"; // pas dit aan
    int baudRate = 9600;

    using (SerialPort port = new SerialPort(portName, baudRate)) {
      port.Open();
      Console.WriteLine($"Verbonden met Arduino op {portName}");
      Console.WriteLine("Wachten op data...\n");

      string? line;
      float? t1 = null, t2 = null, t3 = null, avgTemp = null;
      float? h1 = null, h2 = null, h3 = null, avgHum = null;

      while (true) {
        try {
          line = port.ReadLine().Trim();
          Console.WriteLine(line);

          // Parse met regex
          Match m;

          if ((m = Regex.Match(line, @"Temperature 1= ([0-9.]+)")).Success)
            t1 = float.Parse(m.Groups[1].Value);
          else if ((m = Regex.Match(line, @"Temperature 2= ([0-9.]+)")).Success)
            t2 = float.Parse(m.Groups[1].Value);
          else if ((m = Regex.Match(line, @"Temperature 3= ([0-9.]+)")).Success)
            t3 = float.Parse(m.Groups[1].Value);
          else if ((m = Regex.Match(line, @"Temperature gemiddelde= ([0-9.]+)"))
                       .Success)
            avgTemp = float.Parse(m.Groups[1].Value);
          else if ((m = Regex.Match(line, @"Humidity 1= ([0-9.]+)")).Success)
            h1 = float.Parse(m.Groups[1].Value);
          else if ((m = Regex.Match(line, @"Humidity 2= ([0-9.]+)")).Success)
            h2 = float.Parse(m.Groups[1].Value);
          else if ((m = Regex.Match(line, @"Humidity 3= ([0-9.]+)")).Success)
            h3 = float.Parse(m.Groups[1].Value);
          else if ((m = Regex.Match(line, @"Humidity gemiddelde= ([0-9.]+)"))
                       .Success)
            avgHum = float.Parse(m.Groups[1].Value);

          // Wanneer we de volledige set hebben:
          if (avgTemp.HasValue && avgHum.HasValue) {
            Console.WriteLine($"\n➡️  Gemiddelde temperatuur: {avgTemp:F2} °C");
            Console.WriteLine(
                $"➡️  Gemiddelde luchtvochtigheid: {avgHum:F2} %\n");

            // Hier kun je loggen, opslaan, of grafisch weergeven
            avgTemp = null;
            avgHum = null;
          }
        } catch (TimeoutException) {
        }
      }
    }
  }
}
