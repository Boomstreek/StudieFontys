using System;

public class Program 
{
  public static void Main() 
  {
    { 
// variable blijven binnen de {} staan, zo kan je variable, in dit geval i, later nog een keer gebruiken. in de volgende {} dus.
      Console.WriteLine("While loop basis");
      int i = 1;
      while (i <= 10)
      {
        Console.WriteLine(i);
        i++;
      }
    }
    {
      Console.WriteLine("For loop basis");
      for (int i = 1; i <= 10; i++)
      {
        Console.Write($"{i}, ");
      }

    }
    {
      Console.WriteLine("Loop plus sum");
      int sum = 0;
      for (int i = 1; i <= 10; i++)
      {
        Console.Write($"{i} ");
        sum = sum + i;
        Console.Write($"sum = {sum}, ");
      }
    }
    {
// Je kan in een regel meerder variable opsommen mits van dezelfde type zijn
// Int32 vs Int64, int vs long, hiermee heb ik gespeeld
      Console.WriteLine("Loop plus sum plus user input");
      int sum = 0;
      long userInput = 0;
      Console.WriteLine("Geef een getal aan");
      userInput = Convert.ToInt64(Console.ReadLine());
      for (int i = 1; i <= userInput; i++)
      {
        sum = sum + i;
        Console.Write($"{i} ");
      }
      Console.WriteLine(sum);
    }
    {
// oefenene met Arrays en arrays laten invullen door een for loop
      Console.WriteLine("10 getallen optellen, daarvan som geven en gemiddelde");
      int[] cijfers = new int [10];
// arrays hebben problemen als je bij 1 begint, wat logisch is nu ik erover nadenken.
      for (int i = 0; i < 10; i++)
      {
// in een $"" string werkt {i + 1}, tussen de {} kan je dus rekenen
        Console.Write($"Voor cijfer {i + 1} in: ");
        cijfers[i] = Convert.ToInt32(Console.ReadLine());
      }

      int som = cijfers.Sum();
      double gemiddelde = cijfers.Average();

      Console.WriteLine($"som = {som}");
      Console.WriteLine($"gemiddelde = {gemiddelde}");
    }
    {
      Console.WriteLine("Hier ga ik de kubus, derd machter van vijf ingevoerde getallen teruggeven");
      int[] cijfers = new int [5];

      for (int i = 0; i < 5; i++)
      {
        Console.Write($"Voer cijfer {i + 1} in: ");
        cijfers[i] = Convert.ToInt32(Console.ReadLine());
      }
// Oefenen met foreach loop waarbij ik waaarden uit een array haal
      foreach (int cijfer in cijfers)
      {
          Console.WriteLine(cijfer * cijfer * cijfer);
      }
    }
    {
      Console.WriteLine("Hier ga ik op basis van een input getal ga ik daarvan de keer tafel als output geven (6)");
      int[] cijfers = new int [10];
      int input = Convert.ToInt32(Console.ReadLine());
// dit werkt niet. i blijft 0 omdat alle ints in de array 0 zijn. Ik moet dus geen foreach gebruiken maar een for loop.
/*
      foreach (int i in cijfers)
      {
        Console.WriteLine(input * (i + 1));
      }
      */
      Console.WriteLine("Lets begin:");
      for (int i = 0; i < 10; i++)
      {
        Console.WriteLine(input * (i + 1));
      }
    }
    {
      Console.WriteLine("7, tafel van x laten zien tot x");
      Console.WriteLine("Welke tafel van welke cijfer wil je hebben?");
      int inputTafelVan = Convert.ToInt32(Console.ReadLine());
      Console.WriteLine("Tot hoever, welke cijfer, wil je gaan?");
      int inputTotTafel = Convert.ToInt32(Console.ReadLine());

      Console.WriteLine("Begin");
      for (int i = 1; i <= inputTotTafel; i++)
      {
        Console.WriteLine(inputTafelVan * i);
      }
    }
    {
      Console.WriteLine("Na bekijken van het antwoord van vraag 7 zie ik dat ik het verkeerd heb begrepen. Ik moet gaan oefenen met een loop in een loop. Dit is de herkansing");

      int j, i, n;

      n = Convert.ToInt32(Console.ReadLine());

      for (i = 1; i <= 10; i++)
      {
        for (j = 1; j <= n; j++)
        {
          if (j <= n - 1)
          {
            Console.Write("{0}x{1} = {2}, ", j, i, i * j);
          }
          else
          {
              Console.Write("{0}x{1} = {2}", j, i, i * j);
          }
        }
        Console.Write("\n");
      }
    }
  }
}
