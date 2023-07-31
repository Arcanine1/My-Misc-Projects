package PokerCalculator;

import java.util.ArrayList;

public class Game {

    public Deck deck = new Deck();
    private int numofHands;
    private int intialNumCommonCards;
    public ArrayList<Hand> hands =  new ArrayList<Hand>(); 
    public ArrayList<Card> commonCards =  new ArrayList<Card>(); 
    public ArrayList<Card> intialCommonCards =  new ArrayList<Card>(); 
    private Deck afterIntialCommonCardsDeck;

    @SuppressWarnings("unchecked")
    public Game(int intialNumCommonCards, int numofHands){

        this.numofHands = numofHands;
        this.intialNumCommonCards = intialNumCommonCards;

        //adds common  cards
        for (int i=0; i<intialNumCommonCards; i++){
            commonCards.add(deck.randomCard());
        }   

        afterIntialCommonCardsDeck = (Deck) this.deck.clone();
        intialCommonCards = (ArrayList<Card>) commonCards.clone();
    }
    
    //adds hand
    //make sure its less then 2 cards in hand 
    public void addHand(Hand hand) throws Exception{

        if(hand.hand.size()<2){
            throw new Exception("hand has more than 2 cards");
        }

        if(hand.hand.get(0).equals(hand.hand.get(1))){
            throw new Exception("cards in hand are equal");
        }

        hands.add(hand);

        //removes cards from deck
        for (Card card: hand.hand){
            for (Card commonCard:commonCards){

                if(card.equals(commonCard)){
                     throw new Exception("card in Common Hand");
                }
            }
            afterIntialCommonCardsDeck.deck.remove(card);
            deck.deck.remove(card);
        }

    }

        //adds hand
    //make sure its less then 2 cards in hand 
    public void addCommonCard(Card card) throws Exception{
        for (Card commonCard:commonCards){
            if(card.equals(commonCard)){
                throw new Exception("card in Common Hand");
            }
        }

        afterIntialCommonCardsDeck.deck.remove(card);
        intialCommonCards.add(card);
        commonCards.add(card);
        deck.deck.remove(card);
        intialNumCommonCards++;

    }


    //plays hand with deck after common cards
    //prints out best hand
    //returns player that won
     @SuppressWarnings("unchecked")
    public int simulateHand() {

        //makes hand variables
        for (int i=0; i<numofHands; i++){
            hands.add(new Hand(deck));
        } 

        //adds rest of common  cards
        for (int i=0; i<5-intialNumCommonCards; i++){
            commonCards.add(deck.randomCard());
        }   

        //intializes hands
        for (Hand hand: hands){

            //adds common cards
            for (Card card: commonCards){
                hand.addCard(card);
            }

            //makes sure every player has 2 privte cards
            int size= hand.hand.size();
            for(int i =0; i< 7-size; i++){
                hand.newCard();
            }

            hand.calculateStrenght();

        } 

        //finds best hand
        Hand bestHand = hands.get(0);
        for (Hand hand : hands) {
            if (hand.better(bestHand) == 1){
                bestHand = hand;
            }
        }

        int player = hands.indexOf(bestHand) +1;

        //prints out best hand
        System.out.println("player " +   player ); 
        System.out.println(bestHand + "\n"); 
        bestHand.calculateStrenght();

        for (double d : bestHand.strength) {
            System.out.println(d);
        }
        System.out.println();

        if(hands.get(0).better(hands.get(1))== 0){
            //resets deck and common cards
            deck = (Deck) this.afterIntialCommonCardsDeck.clone();
            commonCards = (ArrayList<Card>) intialCommonCards.clone();
            hands =  new ArrayList<Hand>(); 
            return 3;
        }

        //resets deck and common cards
        deck = (Deck) this.afterIntialCommonCardsDeck.clone();
        commonCards = (ArrayList<Card>) intialCommonCards.clone();
        hands =  new ArrayList<Hand>(); 

        
        return player;
    }
}
