package PokerCalculator;

public class Probability
{
    public static void main(String[] args) throws Exception {

        int randomPlayer = 1;
        int skillsPlayer=1;
        double plays = 10000;
        int [] winners =  new int[randomPlayer+skillsPlayer+1];

        Game game = new Game(0,randomPlayer);
        //game.addCommonCard(new Card (2,14));

        for(int i =0; i<plays; i++){

            //neccessary for each hand of skilled players
            Hand hand = new Hand(game.deck);
            hand.addCard(new Card(0,14));
            hand.addCard(new Card(1,14));
            
            game.addHand(hand);
            winners[game.simulateHand()-1]++;
        }

        int j=0;
        for (int i : winners) {
            System.out.println("Player " + (j+1) + ": "  + i/plays);
            j++;
        }

    }
}