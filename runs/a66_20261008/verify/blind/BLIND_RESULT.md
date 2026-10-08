# A66 blind order test result

| id | word | sensible orders | verdict | notes |
|---|---|---|---|---|
| 8055 | balloon | acb | PASS | Fits the still (man hanging from a hot-air balloon's ropes); 'a passing balloon's rope' is slightly odd for a hot-air balloon but fine. |
| 236 | dolphin | cab | PASS | Video shows a dolphin beside a boat and jumping; no visible race or Mia, but nothing contradicts the story. |
| 7071 | king | bca | PASS | Fits the frames (king in robe and crown on a quad bike splashing through mud puddles). |
| 8056 | bench | bac | PASS | Fits the drawing (man reading on a bench, dog looking up at him). |
| 62 | bag | bca | PASS | Mostly fits: he packs apples, bread, water; in the last frame he actually drags the bag, so 'couldn't lift it' is only roughly shown. |
| 8039 | way | cab | PASS | Fits the frames (woman shovelling a snow path, husky running through it, parents watching from the window). |
| 900001 | select | cab | PASS | Fits the still (doughnut counter, a second hand reaching over the glass); 'reached over the glass' is a bit compressed but clear. |
| 900002 | classical | cba | PASS | Fits the still (bear on cello, fox on violin, chandelier in a palace room). |

## All orders

### 8055

| order | sensible | text | why |
|---|---|---|---|
| abc | no | Tom missed his bus, He held on all the way to work. so he grabbed a passing balloon's rope. | comma then capital 'He'; story jumps to holding on before the balloon |
| acb | yes | Tom missed his bus, so he grabbed a passing balloon's rope. He held on all the way to work. | cause, comma join into lowercase 'so', then the result |
| bac | no | He held on all the way to work. Tom missed his bus, so he grabbed a passing balloon's rope. | 'He' before Tom; effect before cause; ends on a comma-continuation fine but order reversed |
| bca | no | He held on all the way to work. so he grabbed a passing balloon's rope. Tom missed his bus, | 'He held on' with nothing to hold; then comma ends on 'so he grabbed' after already holding |
| cab | no | so he grabbed a passing balloon's rope. Tom missed his bus, He held on all the way to work. | starts lowercase 'so' |
| cba | no | so he grabbed a passing balloon's rope. He held on all the way to work. Tom missed his bus, | starts lowercase 'so'; ends with a comma |

### 236

| order | sensible | text | why |
|---|---|---|---|
| abc | no | The dolphin won easily, so it jumped high into the air to celebrate! Mia's boat raced a dolphin. | 'The dolphin' before it is introduced; race sentence comes after the result |
| acb | no | The dolphin won easily, Mia's boat raced a dolphin. so it jumped high into the air to celebrate! | comma then capital 'Mia's'; 'so it jumped' detached from the win |
| bac | no | so it jumped high into the air to celebrate! The dolphin won easily, Mia's boat raced a dolphin. | starts lowercase 'so' |
| bca | no | so it jumped high into the air to celebrate! Mia's boat raced a dolphin. The dolphin won easily, | starts lowercase 'so' |
| cab | yes | Mia's boat raced a dolphin. The dolphin won easily, so it jumped high into the air to celebrate! | race set up, dolphin wins, celebrates last |
| cba | no | Mia's boat raced a dolphin. so it jumped high into the air to celebrate! The dolphin won easily, | race sentence then 'so it jumped' (cause missing) with no win stated; ends on a comma |

### 7071

| order | sensible | text | why |
|---|---|---|---|
| abc | no | He splashed through every puddle and laughed like a little boy. Tired of his golden carriage, the old king borrowed the gardener's quad bike. | 'He' before the king is named; ends on 'the old king ...' after his deeds |
| acb | no | He splashed through every puddle and laughed like a little boy. the old king borrowed the gardener's quad bike. Tired of his golden carriage, | 'He' before the king; comma then lowercase 'the' but carriage phrase dangles |
| bac | no | Tired of his golden carriage, He splashed through every puddle and laughed like a little boy. the old king borrowed the gardener's quad bike. | comma then capital 'He'; 'the old king' after his deeds |
| bca | yes | Tired of his golden carriage, the old king borrowed the gardener's quad bike. He splashed through every puddle and laughed like a little boy. | comma phrase into 'the old king', then the splashing payoff |
| cab | no | the old king borrowed the gardener's quad bike. He splashed through every puddle and laughed like a little boy. Tired of his golden carriage, | starts lowercase 'the' |
| cba | no | the old king borrowed the gardener's quad bike. Tired of his golden carriage, He splashed through every puddle and laughed like a little boy. | starts lowercase 'the'; ends with a comma |

### 8056

| order | sensible | text | why |
|---|---|---|---|
| abc | no | His dog looks at him. Ben sits on a bench with a book. It wants a walk, not a story! | 'His dog' before Ben is named |
| acb | no | His dog looks at him. It wants a walk, not a story! Ben sits on a bench with a book. | 'His dog' before Ben; ends flatly on setup |
| bac | yes | Ben sits on a bench with a book. His dog looks at him. It wants a walk, not a story! | Ben introduced, dog looks, dog's wish is the punchline |
| bca | no | Ben sits on a bench with a book. It wants a walk, not a story! His dog looks at him. | 'It' would refer to the book; dog appears after the punchline |
| cab | no | It wants a walk, not a story! His dog looks at him. Ben sits on a bench with a book. | 'It' with no referent at the start |
| cba | no | It wants a walk, not a story! Ben sits on a bench with a book. His dog looks at him. | 'It' with no referent; ends flatly |

### 62

| order | sensible | text | why |
|---|---|---|---|
| abc | no | Now he couldn't lift it! Sam packed a picnic bag. He added apples, bread and a big bottle of water. | 'Now he couldn't lift it' before anything is packed |
| acb | no | Now he couldn't lift it! He added apples, bread and a big bottle of water. Sam packed a picnic bag. | result first, 'He' before Sam |
| bac | no | Sam packed a picnic bag. Now he couldn't lift it! He added apples, bread and a big bottle of water. | can't lift it before the heavy items are added (effect before cause) |
| bca | yes | Sam packed a picnic bag. He added apples, bread and a big bottle of water. Now he couldn't lift it! | pack, add heavy items, can't lift it last |
| cab | no | He added apples, bread and a big bottle of water. Now he couldn't lift it! Sam packed a picnic bag. | 'He' before Sam; result before the bag is introduced |
| cba | no | He added apples, bread and a big bottle of water. Sam packed a picnic bag. Now he couldn't lift it! | 'He' before Sam; ends flatly |

### 8039

| order | sensible | text | why |
|---|---|---|---|
| abc | no | Her husky squeezed past and ran down it first. Inside, Dad laughed: "Nice path for the dog!" Anna cleared a way through the snow. | 'Her husky ... down it' with no path or owner introduced |
| acb | no | Her husky squeezed past and ran down it first. Anna cleared a way through the snow. Inside, Dad laughed: "Nice path for the dog!" | 'Her husky ... it' before Anna and the path |
| bac | no | Inside, Dad laughed: "Nice path for the dog!" Her husky squeezed past and ran down it first. Anna cleared a way through the snow. | Dad's joke before anything happens; 'Her husky' with no owner |
| bca | no | Inside, Dad laughed: "Nice path for the dog!" Anna cleared a way through the snow. Her husky squeezed past and ran down it first. | Dad's joke first; 'Her husky' before Anna |
| cab | yes | Anna cleared a way through the snow. Her husky squeezed past and ran down it first. Inside, Dad laughed: "Nice path for the dog!" | path cleared, husky uses it first, Dad's joke last |
| cba | no | Anna cleared a way through the snow. Inside, Dad laughed: "Nice path for the dog!" Her husky squeezed past and ran down it first. | Dad jokes 'path for the dog' before the dog has used it; punchline not last |

### 900001

| order | sensible | text | why |
|---|---|---|---|
| abc | no | His friend got tired of waiting. So she reached over the glass and grabbed three. Max took five minutes to select one doughnut. | 'His friend' before Max; 'she reached' before the doughnut |
| acb | no | His friend got tired of waiting. Max took five minutes to select one doughnut. So she reached over the glass and grabbed three. | 'His friend' before Max is named |
| bac | no | So she reached over the glass and grabbed three. His friend got tired of waiting. Max took five minutes to select one doughnut. | starts 'So she' with no referent |
| bca | no | So she reached over the glass and grabbed three. Max took five minutes to select one doughnut. His friend got tired of waiting. | starts 'So she' with no referent |
| cab | yes | Max took five minutes to select one doughnut. His friend got tired of waiting. So she reached over the glass and grabbed three. | slow choice, friend impatient, friend grabs three last |
| cba | no | Max took five minutes to select one doughnut. So she reached over the glass and grabbed three. His friend got tired of waiting. | 'she' before the friend is introduced; impatience after the action |

### 900002

| order | sensible | text | why |
|---|---|---|---|
| abc | no | The duet was so loud that the chandelier shook! A fox joined in on the violin. Bruno the bear played classical music on his cello. | 'The duet' before any players; fox 'joined in' with nothing to join |
| acb | no | The duet was so loud that the chandelier shook! Bruno the bear played classical music on his cello. A fox joined in on the violin. | 'The duet' first; result before the players |
| bac | no | A fox joined in on the violin. The duet was so loud that the chandelier shook! Bruno the bear played classical music on his cello. | fox 'joined in' with nothing to join |
| bca | no | A fox joined in on the violin. Bruno the bear played classical music on his cello. The duet was so loud that the chandelier shook! | fox 'joined in' first; Bruno introduced after the duet |
| cab | no | Bruno the bear played classical music on his cello. The duet was so loud that the chandelier shook! A fox joined in on the violin. | Bruno plays, then the duet result before the fox joins |
| cba | yes | Bruno the bear played classical music on his cello. A fox joined in on the violin. The duet was so loud that the chandelier shook! | bear plays, fox joins, loud duet shakes the chandelier last |

PASS 8 / FAIL 0
