using System;
using System.IO.Ports;
using System.Threading;

class Program {
  static void Main() {
    string portName = "/dev/ttyUSB0"; // Arduino poort linux, wellicht ooit uitbreiden naar
    int baudRate = 9600;

    SerialPort serial = new SerialPort(portName, baudRate); 
    serial.ReadTimeout = 2000;
    serial.WriteTimeout = 500;

    Console.WriteLine("Bliep Bloep, trying to connect, Bliep Bloep");

    if (serial != null) // check if poort bestaat
    {
      serial.Open();
      if (serial.IsOpen) {
        Console.WriteLine("Bloop Bloop, verbinding is gemaakt." + portName);

        // Even wachten voor arduino poort. Wellicht overbodig but it works :D
        Thread.Sleep(2000);

        byte handshake = 0b00100100;
        Console.WriteLine("Handshake verstuurt");
        serial.Write(new byte[] { handshake }, 0, 1);

        // wachten op reactie
        Thread.Sleep(200);

        bool handshakeGelukt = false;
        int wachtTijd = 0;

        // Wachten op handshake
        while (!handshakeGelukt && wachtTijd < 20) {
          if (serial.BytesToRead > 0) {
            string reactie = serial.ReadLine().Trim();
            Console.WriteLine("Arduino reageert: " + reactie);

            if (reactie == "ACK") {
              handshakeGelukt = true;
            }
          } else {
            Thread.Sleep(100);
            wachtTijd++;
          }
        }

        if (handshakeGelukt) {
          Console.WriteLine("Handshake gelukt!");
          Thread.Sleep(200);

          // Meetcommando sturen
          byte command = 0b10100101;
          serial.Write(new byte[] { command }, 0, 1);
          Console.WriteLine("Meetcommando verstuurd...");

          Thread.Sleep(100);

          bool lezen = true;
          while (lezen) {
            if (serial.BytesToRead > 0) {
              string line = serial.ReadLine().Trim();
              if (line.Length > 0) {
                Console.WriteLine("Arduino zegt: " + line);
              }
            } else {
              lezen = false;
            }
          }
        } else {
          Console.WriteLine("Geen antwoord op handshake ontvangen!");
        }

        serial.Close();
        Console.WriteLine("Verbinding gesloten.");
      } else {
        Console.WriteLine("Kon de poort niet openen.");
      }
    } else {
      Console.WriteLine("Poort niet gevonden!");
    }
  }
}

/*
using System;
using System.IO.Ports;
using System.Threading;

class Program
{
    static void Main()
    {
        string portName = "/dev/ttyUSB0"; // Arduino poort op Linux
        int baudRate = 9600;

        try
        {
            using (SerialPort serial = new SerialPort(portName, baudRate))
            {
                serial.ReadTimeout = 2000; // timeout voor lezen (ms)
                serial.WriteTimeout = 500;

                serial.Open();
                Console.WriteLine("Verbinding gemaakt met Arduino op " +
portName);

                // 🚨 Belangrijk: Arduino reset na poort open, even wachten
                Thread.Sleep(2000); // 2 seconden

                // Meet-commando sturen
                byte command = 0b10100101;
                serial.Write(new byte[] { command }, 0, 1);

                // Even wachten zodat Arduino ACK + JSON kan sturen
                Thread.Sleep(100);

                // Alles lezen dat Arduino stuurt
                while (serial.BytesToRead > 0)
                {
                    try
                    {
                        string line = serial.ReadLine().Trim();
                        if (!string.IsNullOrEmpty(line))
                        {
                            Console.WriteLine("Arduino zegt: " + line);
                        }
                    }
                    catch (TimeoutException)
                    {
                        // timeout lezen, gewoon doorgaan
                        break;
                    }
                }

                serial.Close();
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Fout: " + ex.Message);
        }
    }
}

*/

/*
using System;
using System.IO.Ports;
using System.Threading;
using System.Text.Json;

class Program
{
    static void Main(string[] args)
    {
        // Zet hier de juiste COM-poort en baudrate
        string portName = "/dev/ttyUSB0"; // Pas aan naar jouw Arduino
        int baudRate = 9600;

        using (SerialPort serial = new SerialPort(portName, baudRate))
        {
            serial.ReadTimeout = 2000;
            serial.WriteTimeout = 500;

            try
            {
                serial.Open();
                Console.WriteLine("Verbinding gemaakt met Arduino op " +
portName);

                while (true)
                {
                    // Stuur meet-commando
                    byte[] command = new byte[] { 0b10100101 };
                    serial.Write(command, 0, 1);

                    // Arduino stuurt eerst ACK
                    string ack = serial.ReadLine();
                    if (ack.Trim() == "ACK")
                    {
                        // Arduino stuurt JSON
                        string jsonData = serial.ReadLine();
                        var data =
JsonSerializer.Deserialize<SensorData>(jsonData);

                        Console.WriteLine($"Temperatuur: {data.temperatuur:F2}
°C, Luchtvochtigheid: {data.luchtvochtigheid:F2} %");
                    }
                    else
                    {
                        Console.WriteLine("Geen ACK ontvangen");
                    }

                    Thread.Sleep(2000); // 2 seconden wachten voor de volgende
meting
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Fout: " + ex.Message);
            }
        }
    }

    // JSON mapping klasse
    class SensorData
    {
        public float temperatuur { get; set; }
        public float luchtvochtigheid { get; set; }
    }/dev/ttyUSB0

    */

/* using System;
using System.IO.Ports;
using System.Text.Json;

class Program
{
    static void Main()
    {
        string portName = "/dev/ttyUSB0";
        int baudRate = 9600;

        using (SerialPort port = new SerialPort(portName, baudRate))
        {
            port.ReadTimeout = 5000;
            port.NewLine = "\n";
            port.Open();

            byte measureRequest = 0b10100101;
            port.Write(new byte[] { measureRequest }, 0, 1);
            Console.WriteLine("Meetverzoek verstuurd...");

            try
            {
                string jsonData = port.ReadLine().Trim();
                Console.WriteLine("Ontvangen JSON: " + jsonData);

                SensorData data =
JsonSerializer.Deserialize<SensorData>(jsonData);

                if (data != null)
                {
                    Console.WriteLine($"Temperatuur: {data.temperatuur:F1} °C");
                    Console.WriteLine($"Luchtvochtigheid:
{data.luchtvochtigheid:F1} %");
                }
            }
            catch (TimeoutException)
            {
                Console.WriteLine("Timeout: geen reactie van Arduino binnen 5
seconden.");
            }

            port.Close();
        }
    }
}
*/
