package PokerCalculator;

import java.util.ArrayList;
import java.util.Collections;

public class Hand{

    public ArrayList<Card> hand = new ArrayList<Card>();
    private Deck deck;
    public double [] strength = {0,0,0};

    //creates links deck to hand
    public Hand(Deck deck) {
        this.deck = deck;
    }


    //creates hand without deck
    public Hand(){

    }


    //adds card without deck
    public void addCard(Card card){
        hand.add(card);
    }


    //adds card to hand if less than 7 hands
    public void newCard(){
        if(hand.size()>7){
            return;
        }

        Card card = deck.randomCard();
        hand.add(card);
    }

    public String toString(){
        String s ="";
        for (Card card : hand) {
            s= s+ card.suit + " " + card.card + "\n";
        }
        return s;
    }

    //if same 0
    //if better 1
    //if worse -1
    public int better(Hand hand){

        hand.calculateStrenght();
        this.calculateStrenght();

        for (int i=0; i<3; i++) {
            if(this.strength[i]> hand.strength[i]){
                return 1;
            }
            if(this.strength[i] < hand.strength[i]){
                return -1;
            }
        }

        return 0;
    }

    //returns a double array which defines the strnrght
    //first is how good of a hand (straight flush, 4,etc) goes from 8 - 0
    //second determines how good within a hand (ace high etc)
    public double[] calculateStrenght(){

        //finds high card
        strength[2] = highCard();
    
        //if its a straight flush you are done
        int straightFlush =  straightFlush();
        if(straightFlush != -1){
            strength[0]= 8;
            strength[1]= straightFlush;
            return strength;
        }

        //if its a 4 of a kind you are done
        int fourOfaKind =  fourOfaKind();
        if(fourOfaKind != -1){
            strength[0]= 7;
            strength[1]= fourOfaKind;
            return strength;
        }

        //if its a full house you are done
        double fullHouse =  fullHouse();
        if(fullHouse != -1){
            strength[0]= 6;
            strength[1]= fullHouse;
            return strength;
        }

        //if its a flush you are done
        int flush = flush();
        if(flush != -1){
            strength[0]= 5;
            strength[1]= flush;
            return strength;
        }
        
        //if its a straight you are done
        int straight = straight();
        if(straight != -1){
            strength[0]= 4;
            strength[1]= straight;
            return strength;
        }

        //if its a 3 kind you are done
        int threeOfaKind = threeOfaKind();
        if(threeOfaKind != -1){
            strength[0]= 3;
            strength[1]= threeOfaKind;
            return strength;
        }

        //if its a 2 pair you are done
        double twoPair = twoPair();
        if(twoPair != -1){
            strength[0]= 2;
            strength[1]= twoPair;
            return strength;
        }

        //if its a 2 pair you are done
        int pair = pair();
        if(pair != -1){
            strength[0]= 1;
            strength[1]= pair;
            return strength;
        }

        return strength;
    }

    //determines if Straigh flush
    // if flush return corresponding strenght array
    private int straightFlush (){
        int [] suits = new int [4];
        int suit = -1;

        //counts how many of each suit
        for (Card card:hand){
            suits[card.suit]++;
        }   

        //determines if flush
        for ( int i=0; i<4; i++){
            if(suits[i]>=5){
                suit = i;
            }
        }

        if(suit == -1){
            return -1;
        }

        //creates flush hand
        Hand flushHand =  new Hand();
        for (Card card: hand){
            if(card.suit==suit){
                flushHand.addCard(card);
            }
        }

        //returns things yay
        return flushHand.straight();
    }


    //returns the 4 of a kind card
    //-1 if none
    private int fourOfaKind(){
        ArrayList<Integer> numbers = new ArrayList<Integer>(0);
        
        //creates numbers array
        for (Card card: hand){
            numbers.add(card.card);
        }

        Collections.sort(numbers);

        //determines if 4 of a kind exists
        int streak =1;
        int previousNumber =-100;
        int match =-1;
        for (int number: numbers){

            if(number== previousNumber){
                streak++;
            }
            else{
                streak=1;
            }

            if(streak>=4){
                match = number;
            }
            previousNumber = number;

        }

        return match;
    }
   

    //returns a decimal that represnts the full house
    // 3 of kind + (2 pair)/15
    //ensures the right order
    //returns -1 if no full house
    private double fullHouse(){

        //finds if there is a three of a kind
        int threeOfaKind = this.threeOfaKind();
        if(threeOfaKind == -1){
            return -1;
        }

        // creates pair hand
        Hand pairHand = new Hand();
        for (Card card : hand) {
            if(card.card != threeOfaKind){
                pairHand.addCard(card);
            }
        }

        int pair = pairHand.pair();
        if(pair==-1){
            return-1;
        }

        return (threeOfaKind + pair/15.0);
    }
   
    //determines if flush
    // if flush returns high card
    private int flush (){
        int [] suits = new int [4];
        int suit = -1;

        //counts how many of each suit
        for (Card card:hand){
            suits[card.suit]++;
        }   

        //determines if flush
        for ( int i=0; i<4; i++){
            if(suits[i]>=5){
                suit = i;
            }
        }

        if(suit == -1){
            return -1;
        }

        //determines high card
        int max = -1;
        for (Card card: hand){
            if(card.suit==suit){
                if(card.card > max){
                    max = card.card;
                }
            }
        }

        return max;
    }


    //returns the high card in a straigh if there is a straight
    private int straight(){
        ArrayList<Integer> numbers = new ArrayList<Integer>(0);
        
        //creates numbers array
        for (Card card: hand){
            numbers.add(card.card);
        }

        Collections.sort(numbers);

        // if ace than add a 1 at the begining
        if(numbers.get(numbers.size()-1) == 14){
            numbers.add(0,1);
        }

        //determines if straight exists
        int streak =1;
        int previousNumber =-100;
        int high = -1;
        for (int number: numbers){

            if(number== previousNumber +1){
                streak++;
            }
            else{
                streak=1;
            }

            if(streak>=5){
                high = number;
            }
            previousNumber = number;

        }

        return high;
        
    }

    //returns the 3 of a kind card
    //-1 if none
    private int threeOfaKind(){

        ArrayList<Integer> numbers = new ArrayList<Integer>(0);
        
        //creates numbers array
        for (Card card: hand){
            numbers.add(card.card);
        }

        Collections.sort(numbers);

        //determines if 3 of a kind exists
        int streak =1;
        int previousNumber =-100;
        int match =-1;
        for (int number: numbers){

            if(number== previousNumber){
                streak++;
            }
            else{
                streak=1;
            }

            if(streak>=3){
                match = number;
            }
            previousNumber = number;

        }

        return match;
    }


    //returns a decimal that represnts the 2 pair
    // higher pair + (lower pair)/15
    //ensures the right order
    //returns -1 if no 2 pairs
    private double twoPair(){
        
        //finds if there is a pair
        int highPair = this.pair();
        if(highPair==-1){
            return -1;
        }

        // creates other pair hand
        Hand pairHand = new Hand();
        for (Card card : hand) {
            if(card.card != highPair){
                pairHand.addCard(card);
            }
        }

        int pair = pairHand.pair();
        if(pair==-1){
            return-1;
        }

        return (highPair + pair/15.0);
    }
    

    //returns highest pair
    //-1 if none
    private int pair(){

         ArrayList<Integer> numbers = new ArrayList<Integer>(0);
        
        //creates numbers array
        for (Card card: hand){
            numbers.add(card.card);
        }

        Collections.sort(numbers);

        //finds highest pair
        int streak =1;
        int previousNumber =-100;
        int match =-1;
        for (int number: numbers){

            if(number== previousNumber){
                streak++;
            }
            else{
                streak=1;
            }

            if(streak>=2){
                match = number;
            }
            previousNumber = number;
        }

        return match;
    }



    //returns high card
    private int highCard(){

         ArrayList<Integer> numbers = new ArrayList<Integer>(0);
        
        //creates numbers array
        for (Card card: hand){
            numbers.add(card.card);
        }

        Collections.sort(numbers);

        //finds highest card
        int max= -1;
        for (int number : numbers) {
            if(number>max){
                max=number;
            }
        }

        numbers.remove(Integer.valueOf(max));

        //finds second highest card
        int second= -1;
        for (int number : numbers) {
            if(number>second){
                second=number;
            }
        }

        return max + second/15;
    }

}



