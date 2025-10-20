using System;
using System.IO.System;

namespace ArduinoLuisteren
{
  public class Handshake
  {
    public bool Connect(SerialPort serial, byte handshakeCommand = 0b00100100, int openDelayMs = 2000)
    {
      if (Serial == null)
        throw new ArgumentNullException(nameof(serial));

      return false;
    }
  }
}
