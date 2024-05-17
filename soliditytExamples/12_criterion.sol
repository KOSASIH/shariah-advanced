12. Avoidance of speculation (gharar):
    - Contracts should not involve excessive speculation where the outcome is highly uncertain.
    - Example: A futures contract in commodities where neither party has a genuine intention to deliver or receive the goods, but rather to profit from price movements.
    - Solidity Example:
      ```solidity
      // Not compliant: Speculative futures contract
      contract SpeculativeFutures {
          address public party1;
          address public party2;
          uint256 public futurePrice;
```solidity// Not compliant: Speculative futures contract
      contract SpeculativeFutures {
          address public party1;
          address public party2;
          uint256 public futurePrice;
```