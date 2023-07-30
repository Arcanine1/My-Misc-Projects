package PokerCalculator;

public class Client {
    
    public static void main(String args[]) {
        
        Deck deck = new Deck();
        Hand hand = new Hand(deck);

        hand.newCard();
        hand.newCard();
        hand.newCard();
        hand.newCard();
        hand.newCard();
        hand.newCard();
        hand.newCard();
        hand.newCard();
        hand.newCard();
        hand.newCard();
        hand.newCard();
        hand.newCard();



        System.out.println(hand);

        for (double d : hand.calculateStrenght()) {
            System.out.println(d + " ");
        }
    }
}
