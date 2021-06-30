This is a faction manager for an interactive story.  It is currently incomplete.
The main functions of this program is to automate many things that the author of the story does manually every story turn.
Functions include:setting a per turn income of various resources, increasing income by set amounts, mook unit production and setting amounts,
                  adding/removing/transfering hero units with specified ship types, managing a faction specific resource and interaction thereof.
Raw unit numbers can be visually overwhelming and it can be hard to tell the size of the army just from that alone, for that the Mag system was included which essentially works in the following way:
1 mag = amount of units 10 production buildings can build in a week
so when the display says 'Mags: 1' that is what that means
Mag 2 is double the amount of units of Mag 1 while Mag 3 is double the amount of units of Mag 2.  And so on, doubling the higher the units go.
For example: 2 armies, one with Mag 5 and another with Mag 4 worth of units.  The army with Mag 5 has the numerical superiority by a factor of two.
            If that Mag 5 was a Mag 6 instead then the first army would have a numerical advantage of a factor of 4 and so on.
This system makes it simpler to estimate the relative numbers of an army.


To run the app pysimplegui needs to be installed in the enviroment, all other data imports come from internal classes.
