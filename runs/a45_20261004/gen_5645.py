from gen_5644_5645_5646_5647_lib import write
wom = [(.15,.30,.65,.46),(.14,.31,.66,.46),(.17,.31,.62,.46),(.13,.30,.56,.47),(.08,.31,.62,.47),(.07,.31,.62,.48),(.04,.33,.66,.47),(.03,.33,.67,.47)]
cart = [(.28,.76,.46,.14),(.28,.77,.46,.14),(.26,.77,.48,.14),(.24,.77,.48,.14),(.22,.78,.48,.14),(.22,.79,.48,.14),(.21,.80,.49,.14),(.21,.80,.49,.14)]
write(5645, "A", "behavior", "female",
 [("to wave her arms", "the woman", "female", wom),
  ("to shout with joy", "the woman", "female", wom),
  ("to roll across the floor", "the cart", "female", cart)],
 3.7,
 [("books", .50, .13, "female"), ("a sign", .55, .31, "female"), ("a backpack", .78, .77, "female"), ("a cart", .40, .88, "female")],
 "What is the curly-haired woman doing?", "She is riding on a book cart.", "female",
 "Woman sits on the cart: her box ends below her shoes, the cart box covers the lower cart and wheels. Man in suit too small/overlapping to use. Key word 'behavior' abstract.")
