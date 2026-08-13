# Synthetic reference output — not source text

## Data timing

We construct filing tone using information available in real time. A filing enters the signal set only after its recorded timestamp, and the associated stock first becomes eligible for a portfolio at the end of the following calendar month. This lag prevents the sort from using text before investors could observe and process it. The universe contains U.S. common stocks from 1995 through 2023; portfolios use NYSE breakpoints and value weights, and returns include delisting returns. We fixed 1995–2010 as the discovery period before evaluating the signal in the 2011–2023 holdout. This separation matters: the discovery estimate describes the sample in which the signal was developed, whereas the holdout evaluates whether the relation persists in later, unused data.

## Results and interpretation

The high-minus-low portfolio earns 0.44% per month in the 1995–2010 discovery period and 0.21% per month in the 2011–2023 holdout (t = 2.30). Thus, the return spread remains positive in the prespecified holdout but is less than half its discovery-sample magnitude. Excluding microcaps further reduces the holdout spread to 0.13% per month (t = 1.71). The attenuation indicates that the headline relation is partly concentrated among small stocks and makes the microcap boundary economically relevant rather than a cosmetic robustness check.

These estimates support out-of-sample return predictability under the stated timing rule; they do not establish an implementable trading strategy. All reported spreads are gross. We have not measured turnover, transaction costs, borrow availability for the short leg, or capacity, so we cannot infer a net payoff or practical scalability. The appropriate headline is therefore a real-time-available predictor with a smaller positive holdout spread, not a strategy that earns 0.44% out of sample. An implementation claim would require the missing cost and feasibility evidence, while the economic interpretation should continue to distinguish statistical predictability from tradability.
