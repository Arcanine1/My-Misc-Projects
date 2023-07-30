package PokerCalculator;

import java.util.ArrayList;

public class Game {

    private Deck deck = new Deck();
    private int numCommonCards;
    private int numofHands;

    public Game(int numCommonCards, int numofHands){
        this.numCommonCards = numCommonCards;
        this.numofHands = numofHands;
    }
    
    public Hand play() {

        //creates array lists
        ArrayList<Hand> hands =  new ArrayList<Hand>(); 
        ArrayList<Card> commonCards =  new ArrayList<Card>(); 
       
        //adds common  cards
        for (int i=0; i<numCommonCards; i++){
            commonCards.add(deck.randomCard());
        }   

        //makes hand variables
        for (int i=0; i<numofHands; i++){
            hands.add(new Hand(deck));
        }   

        //intializes hands
        for (Hand hand: hands){

            //adds common cards
            for (Card card: commonCards){
                hand.addCard(card);
            }

            hand.newCard();
            hand.newCard();
            hand.calculateStrenght();

        } 

        //finds best hand
        Hand bestHand = hands.get(0);
        for (Hand hand : hands) {
            if (hand.better(bestHand) == 1){
                bestHand = hand;
            }
            
        }

        //prints out best hand
        System.out.println(bestHand + "\n"); 
        bestHand.calculateStrenght();

        for (double d : bestHand.strength) {
            System.out.println(d);
        }
        System.out.println();

        return bestHand;
    }
}
