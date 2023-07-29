package PokerCalculator;

import java.util.ArrayList;
import java.util.Random;

public class Deck {

    public ArrayList<Card> Deck;
    
    //creates deck of size deck size
    public Deck(int deckSize) throws IllegalAccessException{

        if(deckSize <1  ){
            throw new IllegalAccessException("deckSize must be more than 0");
        }

        for( int i = 0; i<deckSize; i++){
            addNewDeck();
        }
    }

    //Gets Random Card and removes the card from the deck
    public Card randomCard(){
        Random rand = new Random();
        int index = rand.nextInt(Deck.size());
        return Deck.remove(index);
    }

    //add new deck to ArrayList
    private void addNewDeck(){

        for (int suit =1; suit<5; suit++){
                    for (int number =1; number<14; number++){
                        Card card =  new Card (suit,number);
                        Deck.add(card);
            }
        }
    }



}
