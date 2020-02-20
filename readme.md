# Motivation
One day I was taking a carton of eggs out of a fridge when the following question occured to me:
>Can you determine where all the eggs are in a carton without looking inside?

This is equivalent to the following:
>Are there two arrangements of eggs in a carton that feel the same from the outside?
# Proof
It can be proven trivially that every arrangement of zero, one, or two eggs is distinguishable. It takes a little more work, but a human can prove all arrangements of three eggs in a 2 by 6 carton are distinguishable. This also implies that 9, 10, 11, and 12 eggs are also distinguishable, by symmetry. That is as far as I got.
# Method
see `egg.py`

The provided python program lists counter examples which prove the motivating question false. This program assigns every possible arrangement of eggs a key made of nested tuples and integers. This key captures all the information which makes a carton meaningfully distinct. This includes the mass of the carton, the carton's central moment, and the carton's inertia tensor.
# Findings
* You can't tell where the eggs are without looking
* It only takes four eggs to find an equivalent pair
* There are 210 pairs and 10 triples of equivalent cartons
* This is a surprisingly difficult problem
