package validStarrtingCity;
// time complexity O( n^2 )
// space complexity O( 1 )
public class validStartingCitySlow  {

    public int validStartingCity(int[] distances, int[] fuel, int mpg) {
        int numberOfCities = distances.length;
        for (int i = 0; i < distances.length; i++) {
            int milesRemaining = 0;
            for (int j = i; j < i + numberOfCities; j++) {
                if (milesRemaining < 0) {
                    continue;
                }
                int currentCity = j % numberOfCities;
                int currentFuel = fuel[currentCity];
                int distanceToNextCity = distances[currentCity];
                milesRemaining += currentFuel * mpg - distanceToNextCity;

            }
            if (milesRemaining >= 0)
                return i;
        }
        return -1;
    }
}
