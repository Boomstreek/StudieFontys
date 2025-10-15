using System;
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

                SensorData data = JsonSerializer.Deserialize<SensorData>(jsonData);

                if (data != null)
                {
                    Console.WriteLine($"Temperatuur: {data.temperatuur:F1} °C");
                    Console.WriteLine($"Luchtvochtigheid: {data.luchtvochtigheid:F1} %");
                }
            }
            catch (TimeoutException)
            {
                Console.WriteLine("Timeout: geen reactie van Arduino binnen 5 seconden.");
            }

            port.Close();
        }
    }
}

