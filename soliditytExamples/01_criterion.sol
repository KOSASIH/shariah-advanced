1. No involvement in riba (interest): 
    - The contract must not include any clauses that involve the payment or receipt of interest.
    - Example: A loan agreement where the lender charges interest on the principal amount.
    - Solidity Example:
      ```solidity
      // Not compliant: Interest-based loan contract
      contract InterestLoan {
          uint256 public principal;
          uint256 public interestRate;
          address public lender;
          address public borrower;
```solidity// Not compliant: Interest-based loan contract
      contract InterestLoan {
          uint256 public principal;
          uint256 public interestRate;
          address public lender;
          address public borrower;
```
