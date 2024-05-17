21. Prohibition of trading in debt:
    - The contract should not involve the trading of debt at a value different from its face value.
    - Example: A contract where a party buys or sells a loan or debt for a price other than its nominal value.
    - Solidity Example:
      ```solidity
      // Not compliant: Trading debt at a discount
      contract DebtTrading {
          address public seller;
          address public buyer;
          uint256 public debtAmount;
          uint256 public salePrice;
```solidity// Not compliant: Trading debt at a discount
      contract DebtTrading {
          address public seller;
          address public buyer;
          uint256 public debtAmount;
          uint256 public salePrice;
```