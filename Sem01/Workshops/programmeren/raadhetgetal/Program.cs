using System;

class Program
{
    static void Main()
    {
        // Stap 1: Computer bedenkt een willekeurig getal tussen 0 en 1000
        Random random = new Random();
        int geheimGetal = random.Next(0, 1001); // 0 t/m 1000

        int pogingen = 0;
        const int maxPogingen = 10;
        bool geraden = false;

        Console.WriteLine("Welkom bij Raad Het Getal!");
        Console.WriteLine("Probeer het juiste getal te raden tussen 0 en 1000.");
        Console.WriteLine($"Maximaal aantal pogingen is {maxPogingen}.\n");

        while (!geraden && pogingen < maxPogingen)
        {
            Console.Write("Kies een getal tussen 0 en 1000: ");
            string invoer = Console.ReadLine() ?? "";

            if (int.TryParse(invoer, out int gok))
            {
                if (gok == geheimGetal)
                {
                    Console.WriteLine(
                        $"Victory! Je hebt het getal geraden in {pogingen} pogingen.");
                    geraden = true;
                }
                else if (gok < geheimGetal)
                {
                    pogingen++;
                    Console.WriteLine($"Hoger! Pogingen: {pogingen}");
                }
                else
                {
                    pogingen++;
                    Console.WriteLine($"Lager! Pogingen: {pogingen}");
                }
            }
            else
            {
                Console.WriteLine("Geen geldig getal, probeer opnieuw.");
            }
        }

        if (!geraden)
        {
            Console.WriteLine(
                $"Te veel pogingen! Het geheime getal was {geheimGetal}.");
        }

        Console.WriteLine("Druk op een toets om af te sluiten...");
        Console.ReadKey();
    }
}
