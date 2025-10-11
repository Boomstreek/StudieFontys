using System;
using System.IO.Ports;
using System.Text.Json;

class SensorData
{
    public float temperatuur { get; set; }
    public float luchtvochtigheid { get; set; }
}

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

            byte measure = 0b10100101;
            port.Write(new byte[] { measure }, 0, 1);
            Console.WriteLine("Meetverzoek verstuurd...");

            // Wacht tot data beschikbaar is
            DateTime start = DateTime.Now;
            while (port.BytesToRead == 0)
            {
                if ((DateTime.Now - start).TotalMilliseconds > 5000)
                {
                    Console.WriteLine("Timeout: geen reactie van Arduino");
                    return;
                }
            }

            int response = port.ReadByte();
            if (response == 0x55)
            {
                Console.WriteLine("ACK ontvangen, wacht op JSON...");
                string jsonData = port.ReadLine().Trim();
                Console.WriteLine("Ontvangen JSON: " + jsonData);

                SensorData data = JsonSerializer.Deserialize<SensorData>(jsonData);
                Console.WriteLine($"Temperatuur: {data.temperatuur} °C");
                Console.WriteLine($"Luchtvochtigheid: {data.luchtvochtigheid} %");
            }
            else
            {
                Console.WriteLine("NACK ontvangen of fout bij uitlezen.");
            }

            port.Close();
        }
    }
}
