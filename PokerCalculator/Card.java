package PokerCalculator;

public class Card{

    // suit 0-3 for the 4 suits
    // cards 1-13 for the cards
    public int suit;
    public int card;

    public Card(int suit, int card){
        this.suit = suit;
        this.card = card;
    }

    @Override
    public boolean equals(Object o) {

        //if same reference true
        if (this == o) return true;

        //if one is null or diffrent classes false
        if (o == null || getClass() != o.getClass()) return false;

        Card card = (Card) o;

        if(card.suit == this.suit && card.card == this.card){
            return true;
        }

        return false;
    }
}