using System;

class Program
{
    static void Main()
    {
        // Stap 1: Computer bedenkt een willekeurig getal tussen 0 en 1000
        Random random = new Random();
        int geheimGetal = random.Next(0, 1001);  // 0 t/m 1000

        int gok = -1;
        int pogingen = 0; 

        Console.WriteLine("Welkom bij Raad Het Getal!");
        Console.WriteLine("Probeer het juiste getal te raden tussen 0 en 1000.\n");

        // Zolang de gok niet juist is, blijft het spel doorgaan
        while (gok != geheimGetal)
        {
            Console.Write("Kies een getal tussen 0 en 1000: ");

            // Leest de gok van de speler
            string invoer = Console.ReadLine() ?? "";

            // Controleer of invoer een geldig getal is
            if (int.TryParse(invoer, out gok))
            {
                // Controleer of het getal binnen bereik is
                if (gok < 0 || gok > 1000)
                {
                    Console.WriteLine("Getal buiten bereik! Probeer opnieuw.\n");
                    continue;
                }

                if (gok == geheimGetal)
                {
                    Console.WriteLine("🎉 Gewonnen!!! Het juiste getal was " + geheimGetal);
                    Console.WriteLine($"Aantal pogingen: {pogingen}");
                }
                else if (gok > geheimGetal)
                {
                    Console.WriteLine("FOUT! Gok lager ↓\n");
                    pogingen++;
                }
                else
                {
                    Console.WriteLine("FOUT! Gok hoger ↑\n");
                    pogingen++;
                }
            }
            else
            {
                Console.WriteLine("Dat is geen geldig getal. Probeer opnieuw!\n");
            }
        }

        Console.WriteLine("Druk op een toets om af te sluiten...");
        Console.ReadKey();
    }
}

