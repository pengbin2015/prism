# Gradient descent: controlled steps downhill

Original geometric explanation. Six scenes; total duration 180 seconds. English narration: Kokoro `af_heart`.

## 000–025 seconds — A landscape of errors

**Visual:** A parameter enters a model; prediction error becomes a loss landscape.

**Narration:** A machine learning model makes predictions using adjustable numbers called parameters. Training means finding parameter values that reduce prediction error. To see how this works, imagine a model with just one parameter, called w. Each possible value has a corresponding loss. Plot those losses, and we get a landscape.

## 025–050 seconds — Find a local rule

**Visual:** Reveal the quadratic, its minimum, and the starting position.

**Narration:** In this simplified example, the loss is w minus three, squared. The lowest point occurs at three. We can see that because the whole curve is visible. But a training algorithm needs a rule it can apply from its current position. What information tells it which way to move?

## 050–080 seconds — The slope tells us the direction

**Visual:** Show tangent slopes on both sides and at the minimum.

**Narration:** The slope gives us that information. Here, the curve slopes downward as w increases, so moving right reduces the loss. On the other side, the slope is positive, so moving left helps. At the bottom, the slope is zero. The derivative measures this slope. With many parameters, the corresponding collection of derivatives is called the gradient.

## 080–110 seconds — Take one calculated step

**Visual:** Build the update equation; calculate −1 − 0.2(−8) = 0.6.

**Narration:** Gradient descent moves opposite the gradient. Take the current parameter, subtract the gradient multiplied by a learning rate, and repeat. Starting at minus one, our slope is minus eight. With a learning rate of zero point two, the next parameter is zero point six. Subtracting a negative slope moves us right, toward lower loss.

## 110–145 seconds — Choose a controlled step

**Visual:** Repeat updates; compare three rates with the same initial state, scale, and update count.

**Narration:** Repeat the same calculation, and the point approaches the bottom. The learning rate controls the size of each step. A small rate makes steady but slow progress. A suitable rate gets there faster. A rate that is too large can jump across the valley and move farther away. For this curve, positive rates below one converge. At one, the point oscillates. Above one, it moves farther away. A downhill direction does not guarantee a good step.

## 145–180 seconds — The same idea in more dimensions

**Visual:** Build elliptical contours, exact gradient arrows, a descent path, and the general update rule.

**Narration:** Real models usually have many parameters. We can picture two of them as positions on a contour map. The gradient points toward the steepest local increase; its negative points toward the steepest local decrease. Complex landscapes may contain several valleys, so gradient descent does not guarantee the best possible solution. But the working rule stays the same: measure the slope, take a controlled step, and repeat.
