# Our Blackjack Game House Rules

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1 depending if you went over 21
- Use the folowinglist as the deck of cards:

`cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]`

- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn. 
- The computer is the dealer

The goal of the game is to get cards that add up to the largest number, without goint over 21. If the cards add up to more than 21, it's a BUST and you lose immediately. If scores are equal, it's a draw. If a dealer has a hand <17, dealer must take another card.