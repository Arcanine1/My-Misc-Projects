package PokerCalculator;

public class Probability
{
    public static void main(String[] args) throws Exception {

        int randomPlayer = 5;
        int skillsPlayer=1;
        double plays = 100000;
        int [] winners =  new int[randomPlayer+skillsPlayer];

        Game game = new Game(0,randomPlayer);

        for(int i =0; i<plays; i++){

            //neccessary for each hand of skilled players
            Hand hand = new Hand();
            hand.addCard(new Card(0,14));
            hand.addCard(new Card(1,14));

            game.addHand(hand);
            winners[game.simulateHand()-1]++;
        }

        int j=0;
        for (int i : winners) {
            System.out.println("Player " + j + ": "  + i/plays);
            j++;
        }

    }
}