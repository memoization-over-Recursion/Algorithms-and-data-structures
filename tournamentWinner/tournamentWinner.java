package tournamentWinner;
import java.util.*;

// time complexity O( n )
// space complexity O( k )
class tournamentWinner {

    public int HOME_TEAM_WON = 1;

    public String tournamentWinners(
            ArrayList<ArrayList<String>> competitions, ArrayList<Integer> results) {
        String currentBestTeam = "";
        HashMap<String, Integer> scores = new HashMap<String, Integer>();
        scores.put(currentBestTeam, 0);

        for (int idx = 0; idx < competitions.size(); idx++) {
            ArrayList<String> competition = competitions.get(idx);
            int result = results.get(idx);

            String homeTeam = competition.get(0);
            String awayTeam = competition.get(1);

            String winningTeam = (result == HOME_TEAM_WON) ? homeTeam : awayTeam;

            updateScores(winningTeam, 3, scores);

            if (scores.get(winningTeam) > scores.get(currentBestTeam)) {
                currentBestTeam = winningTeam;
            }
        }
        return currentBestTeam;
    }

    public void updateScores(String team, int points, HashMap<String, Integer> scores) {
        if (scores.containsKey(team)) {
            scores.put(team, scores.get(team) + 3);
        } else {
            scores.put(team, 3);
        }
    }
}
