import java.util.*;
//time complexity O( nlog(n) )
//space complexity O( 1 )
public class classPhoto {

    public boolean classPhotos(
            ArrayList<Integer> redShirtHeights, ArrayList<Integer> blueShirtHeights) {
        Collections.sort(redShirtHeights, Collections.reverseOrder());
        Collections.sort(blueShirtHeights, Collections.reverseOrder());
        Boolean be = (redShirtHeights.get(0) < blueShirtHeights.get(0)) ? true : false;
        for (int i = 0; i < blueShirtHeights.size(); i++) {
            int b = blueShirtHeights.get(i);
            int r = redShirtHeights.get(i);
            if (be) {
                if (r >= b)
                    return false;
            } else {
                if (b >= r)
                    return false;
            }
        }

        return true;
    }
}
