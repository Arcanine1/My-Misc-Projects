package PokerCalculator;

public class Probability
{
    public static void main(String[] args) throws Exception {

        int [] winners =  new int[10];

        for(int i =0; i<1000; i++){}
            Game game = new Game(3,9);

            Hand hand = new Hand();
            hand.addCard(new Card(0,14));
            hand.addCard(new Card(1,14));

            game.addHand(hand);

            winners[game.simulateHand()-1]++;
        }

    }
}