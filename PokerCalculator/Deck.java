package PokerCalculator;

import java.util.ArrayList;
import java.util.Random;

public class Deck {

    public ArrayList<Card> deck = new ArrayList<Card>();
    
    //creates deck of size deck size
    public Deck(){
        for (int suit =0; suit<4; suit++){
                    for (int number =2; number<15; number++){
                        Card card =  new Card (suit,number);
                        deck.add(card);
            }
    }
}

    //Gets Random Card and removes the card from the deck
    public Card randomCard(){
        Random rand = new Random();
        int index = rand.nextInt(deck.size());
        return deck.remove(index);
    }
}
