import java.util.*;
// time complexity O( n )
// sapce complexity O( 1 )
class spinRings {
  public static void spinRing(List<List<Integer>> array) {
    int SR = 0;
    int ER = array.size() - 1;
    int SC = 0;
    int EC = array.size() - 1;

    while( SR < ER && SC < EC){
      int current = array.get(SR).get(EC);
      for( int col = EC ; col > SC; col-- ){
        array.get( SR ).set( col , array.get( SR ).get( col - 1 ) );
      }
      for( int row = SR ; row < ER ; row++ ){
        array.get( row ).set( SC , array.get( row + 1 ).get( SC ) );
      }
      for( int col = SC ; col < EC; col++ ){
        array.get( ER ).set(col , array.get( ER ).get( col + 1 ) );
      }
      for( int row = ER ; row > SR + 1; row-- ){
        array.get( row ).set(ER , array.get( row - 1 ).get( ER ) );
      }

      array.get( SR+1 ).set(EC , current);
      ER--;
      EC--;
      SR++;
      SC++;
    }
    
  }
}
