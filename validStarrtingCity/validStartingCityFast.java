package validStarrtingCity;
// time complexity O( n )
// space complexity O( 1 )
public class validStartingCityFast {

    public int validStartingCity(int[] distances, int[] fuel, int mpg) {
        int numberOfCities = distances.length;
        int milesLeft = 0;
        int minMiles = 0;
        int minCity = 0;
        for (int i = 1; i < numberOfCities; i++) {
            int currentFuel = fuel[i - 1];
            int distanceToNextCity = distances[i - 1];
            milesLeft += currentFuel * mpg - distanceToNextCity;

            if (milesLeft < minMiles) {
                minCity = i;
                minMiles = milesLeft;
            }
        }
        return minCity;
    }
}
