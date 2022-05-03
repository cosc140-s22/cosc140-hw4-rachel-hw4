# COSC140 homework 4

## Homework feedback

 * How long did you spend on this homework?
   A bit, maybe around a few hours

 * What did you think about it?  What was good?  What could be improved?
   I liked the hw, I thought the instructions were pretty clear for the most part. I'm just worried I may have missed a step or something
## Feedback

N

The `age_range` method in your model class needs just a little bit more work.  If maximum age is -1, your method should return "Ages 1 and up" (if minimum age is 1).  If you run ./manage.py test you'll see that it doesn't quite do that.

Once you fix that, you'll see one more problem when you run ./manage.py test.  Consider the order if your `elif` parts in that method -- that's what is causing the issue.

--

S 

Everything looks great now!
